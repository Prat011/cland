from typing import List
from fastembed import FastEmbed
from .base import BaseEmbedding

class FastEmbedEmbedding(BaseEmbedding):
    def __init__(self, model_name: str = "BAAI/bge-small-en-v1.5"):
        self.model = FastEmbed(model_name=model_name)

    def embed_documents(self, documents: List[str]) -> List[List[float]]:
        return list(self.model.embed(documents))

    def embed_query(self, query: str) -> List[float]:
        return list(self.model.embed([query]))[0]