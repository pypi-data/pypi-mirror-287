import os
import re
import torch
import numpy as np
import pandas as pd
from tqdm.auto import tqdm
import textwrap
from sentence_transformers import SentenceTransformer, util
from transformers import AutoTokenizer, AutoModelForCausalLM

class QuickRAG:
    def __init__(self, pdf_path, embedding_model_name="all-mpnet-base-v2", llm_model_name="google/gemma-2b-it", use_quantization=True, huggingface_token=None):
        self.pdf_path = pdf_path
        self.embedding_model_name = embedding_model_name
        self.llm_model_name = llm_model_name
        self.use_quantization = use_quantization
        self.huggingface_token = huggingface_token
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        self.embedding_model = None
        self.llm_model = None
        self.tokenizer = None
        self.embeddings = None
        self.pages_and_chunks = None

    def process_pdf(self):
        import fitz  # pymupdf

        def text_formatter(text):
            return text.replace("\n", " ").strip()

        def open_and_read_pdf(pdf_path):
            doc = fitz.open(pdf_path)
            pages_and_texts = []
            for page_number, page in tqdm(enumerate(doc), desc="Processing PDF pages", total=len(doc)):
                text = page.get_text()
                text = text_formatter(text)
                pages_and_texts.append({
                    'page_number': page_number,
                    "page_char_count": len(text),
                    "page_word_count": len(text.split()),
                    "page_sentence_count_raw": len(text.split(". ")),
                    "page_token_count": len(text) // 4,
                    "text": text
                })
            return pages_and_texts

        pages_and_texts = open_and_read_pdf(self.pdf_path)

        import spacy
        nlp = spacy.load("en_core_web_sm")

        for item in tqdm(pages_and_texts, desc="Processing sentences"):
            doc = nlp(item["text"])
            item["sentences"] = [str(sent) for sent in doc.sents]
            item["page_sentence_count_spacy"] = len(item["sentences"])

        num_sentence_chunk_size = 10

        def split_list(input_list, split_size=num_sentence_chunk_size):
            return [input_list[i:i + split_size] for i in range(0, len(input_list), split_size)]

        for item in tqdm(pages_and_texts, desc="Chunking sentences"):
            item["sentence_chunks"] = split_list(input_list=item["sentences"])
            item["num_chunks"] = len(item["sentence_chunks"])

        pages_and_chunks = []
        for item in tqdm(pages_and_texts, desc="Processing chunks"):
            for sentence_chunk in item["sentence_chunks"]:
                joined_sentence_chunk = " ".join(sentence_chunk).strip()
                joined_sentence_chunk = re.sub(r'\.([A-Z])', r'. \1', joined_sentence_chunk)
                chunk_dict = {
                    "page_number": item["page_number"],
                    "sentence_chunk": joined_sentence_chunk,
                    "chunk_char_count": len(joined_sentence_chunk),
                    "chunk_word_count": len(joined_sentence_chunk.split()),
                    "chunk_token_count": len(joined_sentence_chunk) // 4
                }
                pages_and_chunks.append(chunk_dict)

        min_token_length = 30
        self.pages_and_chunks = [chunk for chunk in pages_and_chunks if chunk["chunk_token_count"] > min_token_length]

    def create_embeddings(self):
        self.embedding_model = SentenceTransformer(model_name_or_path=self.embedding_model_name, device=self.device)
        text_chunks = [item["sentence_chunk"] for item in self.pages_and_chunks]
        self.embeddings = self.embedding_model.encode(text_chunks, batch_size=32, convert_to_tensor=True, show_progress_bar=True)

    def load_llm(self):
        model_kwargs = {
            "torch_dtype": torch.float16,
            "low_cpu_mem_usage": True,
        }

        if self.use_quantization and torch.cuda.is_available():
            try:
                from transformers import BitsAndBytesConfig
                quantization_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.float16)
                model_kwargs["quantization_config"] = quantization_config
            except ImportError:
                print("BitsAndBytesConfig not available. Falling back to non-quantized model.")

        self.llm_model = AutoModelForCausalLM.from_pretrained(
            pretrained_model_name_or_path=self.llm_model_name,
            token=self.huggingface_token,
            device_map="auto",
            **model_kwargs
        )
        
        self.tokenizer = AutoTokenizer.from_pretrained(
            pretrained_model_name_or_path=self.llm_model_name,
            token=self.huggingface_token
        )

    def retrieve_relevant_resources(self, query, n_resources_to_return=5):
        query_embedding = self.embedding_model.encode(query, convert_to_tensor=True)
        dot_scores = util.dot_score(query_embedding, self.embeddings)[0]
        scores, indices = torch.topk(input=dot_scores, k=n_resources_to_return)
        return scores, indices

    def prompt_formatter(self, query, context_items):
        context = "\n".join([f"- {item['sentence_chunk']}" for item in context_items])
        base_prompt = f"""Based on the provided context, please answer the following query:

Query: {query}

Context:
{context}

Answer:"""
        return base_prompt

    def ask(self, query, temperature=0.7, max_new_tokens=1024, format_answer_text=True, return_answer_only=True):
        scores, indices = self.retrieve_relevant_resources(query)
        context_items = [self.pages_and_chunks[i] for i in indices]
        for item, score in zip(context_items, scores):
            item["score"] = score.item()

        prompt = self.prompt_formatter(query, context_items)
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        
        with torch.no_grad():
            outputs = self.llm_model.generate(
                **inputs,
                temperature=temperature,
                do_sample=True,
                max_new_tokens=max_new_tokens,
                pad_token_id=self.tokenizer.eos_token_id
            )
        
        output_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        if format_answer_text:
            output_text = output_text.replace(query, "").replace("<bos>", "").replace("<eos>", "").replace("<start_of_turn>", "")
            output_text = re.sub(r'Based on the provided context.*?Answer:', '', output_text, flags=re.DOTALL)
            output_text = output_text.strip()

        if return_answer_only:
            return output_text

        return output_text, context_items

    @staticmethod
    def print_wrapped(text, wrap_length=100):
        wrapped_text = textwrap.fill(text, wrap_length)
        print(wrapped_text)

# Usage example
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Run QuickRAG on a PDF file")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("--token", help="HuggingFace API token", default=None)
    parser.add_argument("--query", help="Query to ask", default="What are the main topics discussed in this document?")
    args = parser.parse_args()

    rag = QuickRAG(args.pdf_path, huggingface_token=args.token)
    rag.process_pdf()
    rag.create_embeddings()
    rag.load_llm()

    answer = rag.ask(args.query)
    print(f"Query: {args.query}")
    QuickRAG.print_wrapped(f"Answer: {answer}")