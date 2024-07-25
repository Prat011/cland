from typing import List
import openai
from .base import BaseEmbedding

class OpenAIEmbedding(BaseEmbedding):
    def __init__(self, api_key: str, model: str = "text-embedding-ada-002"):
        openai.api_key = api_key
        self.model = model

    def embed_documents(self, documents: List[str]) -> List[List[float]]:
        embeddings = openai.Embedding.create(input=documents, model=self.model)
        return [e.embedding for e in embeddings.data]

    def embed_query(self, query: str) -> List[float]:
        embedding = openai.Embedding.create(input=[query], model=self.model)
        return embedding.data[0].embedding
