import numpy as np
from uuid import uuid4
from typing import Optional, Dict, Any, List
from .storage import DiskStorage, SQLiteStorage
from .config import load_config
from .llm.base import BaseLLM
from .llm.openai_llm import OpenAILLM  
import re
from collections import Counter

class RedCache:
    def __init__(self, storage_backend=None, vector_size=100, llm: Optional[BaseLLM] = None):
        if storage_backend is None:
            storage_backend = DiskStorage()
        self.storage = storage_backend
        self.user_memories = self.storage.load()
        self.vector_data = {}
        self.vector_index = {}
        self.vector_size = vector_size
        self.vocabulary = set()
        self.llm = llm
        self._rebuild_vector_data()

   
    @classmethod
    def from_config(cls, config):
        storage_config = config.get("storage", {})
        storage_backend = storage_config.get("backend", "disk")  
        if storage_backend == "disk":
            from .storage import DiskStorage
            storage = DiskStorage()
        elif storage_backend == "sqlite":
            from .storage import SQLiteStorage
            storage = SQLiteStorage()
        else:
            raise ValueError(f"Unsupported storage backend: {storage_backend}")

        llm_config = config.get("llm", {}) 
        llm = None
        if llm_config:
            provider = llm_config.get("provider")
            if provider == "openai":
                from .llm.openai_llm import OpenAILLM
                llm = OpenAILLM(llm_config.get("config", {}))
            else:
                raise ValueError(f"Unsupported LLM provider: {provider}")

        return cls(storage_backend=storage, llm=llm)

    def _rebuild_vector_data(self):
        for user_memories in self.user_memories.values():
            for memory_id, memory in user_memories.items():
                self.vector_data[memory_id] = np.array(memory['vector'])
                self._update_index(memory_id, self.vector_data[memory_id])

    def _preprocess_text(self, text):
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
        return ' '.join(text.split())

    def _vectorize_text(self, text):
        preprocessed_text = self._preprocess_text(text)
        self.vocabulary.update(preprocessed_text.split())
        
        if len(self.vocabulary) < self.vector_size:
            vector = np.zeros(self.vector_size)
            word_counts = Counter(preprocessed_text.split())
            for i, word in enumerate(self.vocabulary):
                vector[i] = word_counts[word]
        else:
            vector = np.zeros(self.vector_size)
            words = preprocessed_text.split()
            for word in words:
                vector[hash(word) % self.vector_size] += 1
        
        norm = np.linalg.norm(vector)
        return vector if norm == 0 else vector / norm

    def add(self, text, user_id, category="general"):
        vector = self._vectorize_text(text)
        memory_id = str(uuid4())
        
        memory = {
            "id": memory_id,
            "text": text,
            "metadata": {
                "data": text,
                "category": category
            },
            "vector": vector.tolist()
        }
        
        if user_id not in self.user_memories:
            self.user_memories[user_id] = {}
        
        self.user_memories[user_id][memory_id] = memory
        self.vector_data[memory_id] = vector
        self._update_index(memory_id, vector)
        
        self.storage.save(self.user_memories)
        
        return [{
            "id": memory_id,
            "event": "add",
            "data": text
        }]

    def get_all(self, user_id):
        return list(self.user_memories.get(user_id, {}).values())

    def _update_index(self, vector_id, vector):
        for existing_vector_id, existing_vector in self.vector_data.items():
            similarity = np.dot(vector, existing_vector)
            if existing_vector_id not in self.vector_index:
                self.vector_index[existing_vector_id] = {}
            self.vector_index[existing_vector_id][vector_id] = similarity

    def search(self, query, user_id, num_results=5):
        query_vector = self._vectorize_text(query)
        results = []
        
        if user_id in self.user_memories:
            for memory in self.user_memories[user_id].values():
                similarity = np.dot(query_vector, np.array(memory["vector"]))
                results.append((memory, similarity))
        
        results.sort(key=lambda x: x[1], reverse=True)
        return [
            {**memory, "score": float(score)}
            for memory, score in results[:num_results]
        ]

    def update(self, memory_id, data, user_id):
        if user_id not in self.user_memories or memory_id not in self.user_memories[user_id]:
            raise ValueError("Memory not found")
        
        memory = self.user_memories[user_id][memory_id]
        memory["text"] = data
        memory["metadata"]["data"] = data
        new_vector = self._vectorize_text(data)
        memory["vector"] = new_vector.tolist()
        
        self.vector_data[memory_id] = new_vector
        self._update_index(memory_id, new_vector)
        
        self.storage.save(self.user_memories)
        
        return {
            "id": memory_id,
            "event": "update",
            "data": data
        }

    def delete(self, memory_id, user_id):
        if user_id in self.user_memories and memory_id in self.user_memories[user_id]:
            del self.user_memories[user_id][memory_id]
            del self.vector_data[memory_id]
            for existing_vector_id in self.vector_index:
                if memory_id in self.vector_index[existing_vector_id]:
                    del self.vector_index[existing_vector_id][memory_id]
            
            self.storage.save(self.user_memories)

    def delete_all(self, user_id):
        if user_id in self.user_memories:
            for memory_id in list(self.user_memories[user_id].keys()):
                self.delete(memory_id, user_id)
            del self.user_memories[user_id]
            
            self.storage.save(self.user_memories)

    def reset(self):
        self.user_memories.clear()
        self.vector_data.clear()
        self.vector_index.clear()
        self.storage.save(self.user_memories)

    def enhance_memory(self, text: str, user_id: str, category: str = "general"):
        if not self.llm:
            raise ValueError("LLM not configured. Cannot enhance memory.")
        prompt = f"Enhance the following memory with additional relevant details:\n\n{text}"
        enhanced_text = self.llm.generate(prompt)
        return self.add(enhanced_text, user_id, category)

    def generate_summary(self, user_id: str) -> str:
        if not self.llm:
            raise ValueError("LLM not configured. Cannot generate summary.")
        memories = self.get_all(user_id)
        memory_texts = [memory['text'] for memory in memories]
        prompt = f"Summarize the following memories:\n\n" + "\n".join(memory_texts)
        return self.llm.generate(prompt) 