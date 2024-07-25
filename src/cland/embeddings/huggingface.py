from typing import List
from sentence_transformers import SentenceTransformer
from .base import BaseEmbedding

class HuggingFaceEmbedding(BaseEmbedding):
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, documents: List[str]) -> List[List[float]]:
        return self.model.encode(documents).tolist()

    def embed_query(self, query: str) -> List[float]:
        return self.model.encode([query])[0].tolist()
