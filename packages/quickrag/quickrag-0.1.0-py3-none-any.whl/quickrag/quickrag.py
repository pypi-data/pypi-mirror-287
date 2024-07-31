# quickrag.py

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
                    'page_number': page_number - 41,
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
        base_prompt = """Based on the following context items, please answer the query.
                     Give yourself room to think by extracting relevant passages from the context before answering the query.
                     Don't return the thinking, only return the answer.
                     Make sure your answers are as explanatory as possible.
                     Use the following examples as reference (and only for reference) for the ideal answer style.
                     \nExample 1:
                     Query: What are the fat-soluble vitamins?
                     Answer: The fat-soluble vitamins include Vitamin A, Vitamin D, Vitamin E, and Vitamin K. These vitamins are absorbed along with fats in the diet and can be stored in the body's fatty tissue and liver for later use. Vitamin A is important for vision, immune function, and skin health. Vitamin D plays a critical role in calcium absorption and bone health. Vitamin E acts as an antioxidant, protecting cells from damage. Vitamin K is essential for blood clotting and bone metabolism.
                     \nExample 2:
                     Query: What are the causes of type 2 diabetes?
                     Answer: Type 2 diabetes is often associated with overnutrition, particularly the overconsumption of calories leading to obesity. Factors include a diet high in refined sugars and saturated fats, which can lead to insulin resistance, a condition where the body's cells do not respond effectively to insulin. Over time, the pancreas cannot produce enough insulin to manage blood sugar levels, resulting in type 2 diabetes. Additionally, excessive caloric intake without sufficient physical activity exacerbates the risk by promoting weight gain and fat accumulation, particularly around the abdomen, further contributing to insulin resistance.
                     \nExample 3:
                     Query: What is the importance of hydration for physical performance?
                     Answer: Hydration is crucial for physical performance because water plays key roles in maintaining blood volume, regulating body temperature, and ensuring the transport of nutrients and oxygen to cells. Adequate hydration is essential for optimal muscle function, endurance, and recovery. Dehydration can lead to decreased performance, fatigue, and increased risk of heat-related illnesses, such as heat stroke. Drinking sufficient water before, during, and after exercise helps ensure peak physical performance and recovery.
                     \nNow use the following context items to answer the user query:
                     {context}
                     \nRelevant passages: <extract relevant passages from the context here>
                     User query: {query}
                     Answer:"""
        prompt = base_prompt.format(context=context, query=query)
        dialogue_template = [{'role': 'user', 'content': base_prompt}]
        prompt = self.tokenizer.apply_chat_template(conversation=dialogue_template, tokenize=False, add_generation_prompt=False)
        return prompt

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
            output_text = re.sub(r'user\nBased on the following.*?Answer:', '', output_text, flags=re.DOTALL)

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