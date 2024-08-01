import os
import re
import torch
import numpy as np
import pandas as pd
from tqdm.auto import tqdm
import textwrap
from sentence_transformers import SentenceTransformer, util
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

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
        import fitz

        def text_formatter(text):
            return text.replace("\n", " ").strip()

        def open_and_read_pdf(pdf_path):
            doc = fitz.open(pdf_path)
            pages_and_texts = []
            for page_number, page in tqdm(enumerate(doc)):
                text = page.get_text()
                text = text_formatter(text)
                pages_and_texts.append({
                    'page_number': page_number,
                    "page_char_count": len(text),
                    "page_word_count": len(text.split(" ")),
                    "page_sentence_count_raw": len(text.split(". ")),
                    "page_token_count": len(text) / 4,
                    "text": text
                })
            return pages_and_texts

        pages_and_texts = open_and_read_pdf(self.pdf_path)

        from spacy.lang.en import English
        nlp = English()
        nlp.add_pipe("sentencizer")

        for item in tqdm(pages_and_texts):
            item["sentences"] = list(nlp(item["text"]).sents)
            item["sentences"] = [str(sentence) for sentence in item["sentences"]]
            item["page_sentence_count_spacy"] = len(item["sentences"])

        num_sentence_chunk_size = 10

        def split_list(input_list, split_size=num_sentence_chunk_size):
            return [input_list[i: i + split_size] for i in range(0, len(input_list), split_size)]

        for item in tqdm(pages_and_texts):
            item["sentence_chunks"] = split_list(input_list=item["sentences"], split_size=num_sentence_chunk_size)
            item["num_chunks"] = len(item["sentence_chunks"])

        pages_and_chunks = []
        for item in tqdm(pages_and_texts):
            for sentence_chunk in item["sentence_chunks"]:
                chunk_dict = {}
                chunk_dict["page_number"] = item["page_number"]
                joined_sentence_chunk = "".join(sentence_chunk).replace(" ", " ").strip()
                joined_sentence_chunk = re.sub(r'\.([A-Z])', r'. \1', joined_sentence_chunk)
                chunk_dict["sentence_chunk"] = joined_sentence_chunk
                chunk_dict["chunk_char_count"] = len(joined_sentence_chunk)
                chunk_dict["chunk_word_count"] = len([word for word in joined_sentence_chunk.split(" ")])
                chunk_dict["chunk_token_count"] = len(joined_sentence_chunk) / 4
                pages_and_chunks.append(chunk_dict)

        min_token_length = 30
        self.pages_and_chunks = [chunk for chunk in pages_and_chunks if chunk["chunk_token_count"] > min_token_length]

    def create_embeddings(self):
        self.embedding_model = SentenceTransformer(model_name_or_path=self.embedding_model_name, device=self.device)
        text_chunks = [item["sentence_chunk"] for item in self.pages_and_chunks]
        self.embeddings = self.embedding_model.encode(text_chunks, batch_size=32, convert_to_tensor=True, show_progress_bar=True)

    def load_llm(self):
        if self.use_quantization and torch.cuda.is_available():
            quantization_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_compute_dtype=torch.float16
            )
            self.llm_model = AutoModelForCausalLM.from_pretrained(
                pretrained_model_name_or_path=self.llm_model_name,
                torch_dtype=torch.float16,
                quantization_config=quantization_config,
                low_cpu_mem_usage=False,
                token=self.huggingface_token
            )
        else:
            self.llm_model = AutoModelForCausalLM.from_pretrained(
                pretrained_model_name_or_path=self.llm_model_name,
                torch_dtype=torch.float16,
                low_cpu_mem_usage=False,
                token=self.huggingface_token
            )
        
        self.tokenizer = AutoTokenizer.from_pretrained(
            pretrained_model_name_or_path=self.llm_model_name,
            token=self.huggingface_token
        )
        self.llm_model.to(self.device)

    def retrieve_relevant_resources(self, query, n_resources_to_return=5):
        query_embedding = self.embedding_model.encode(query, convert_to_tensor=True)
        dot_scores = util.dot_score(query_embedding, self.embeddings)[0]
        scores, indices = torch.topk(input=dot_scores, k=n_resources_to_return)
        return scores, indices

    def prompt_formatter(self, query, context_items):
        context = " - " + "\n- ".join([item["sentence_chunk"] for item in context_items])
        base_prompt = f"""Based on the provided context, please answer the following query:
                         \n{query}
                         \nContext:
                         {context}
                         \nAnswer:"""
        return base_prompt

    def ask(self, query, temperature=0.7, max_new_tokens=1024, format_answer_text=True, return_answer_only=True):
        scores, indices = self.retrieve_relevant_resources(query)
        context_items = [self.pages_and_chunks[i] for i in indices]
        for i, item in enumerate(context_items):
            item["score"] = scores[i].cpu()

        prompt = self.prompt_formatter(query, context_items)
        input_ids = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        outputs = self.llm_model.generate(**input_ids, temperature=temperature, do_sample=True, max_new_tokens=max_new_tokens)
        output_text = self.tokenizer.decode(outputs[0])

        if format_answer_text:
            output_text = output_text.replace(query, "").replace("<bos>", "").replace("<eos>", "").replace("<start_of_turn>", "")
            output_text = re.sub(r'Based on the provided context.*?Answer:', '', output_text, flags=re.DOTALL)

        if return_answer_only:
            return output_text

        return output_text, context_items

    def print_wrapped(self, text, wrap_length=100):
        wrapped_text = textwrap.fill(text, wrap_length)
        print(wrapped_text)

# Usage example
if __name__ == "__main__":
    rag = QuickRAG("path/to/your/pdf.pdf", huggingface_token="YOUR_TOKEN")
    rag.process_pdf()
    rag.create_embeddings()
    rag.load_llm()

    query = "What are the macronutrients, and what roles do they play in the human body?"
    answer = rag.ask(query)
    print(f"Query: {query}")
    rag.print_wrapped(f"Answer: {answer}")
