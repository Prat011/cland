import pinecone
from typing import List, Dict, Any
from .base import BaseVectorStore

class PineconeVectorStore(BaseVectorStore):
    def __init__(self, api_key: str, environment: str, index_name: str):
        pinecone.init(api_key=api_key, environment=environment)
        self.index = pinecone.Index(index_name)

    def add_embeddings(self, embeddings: List[List[float]], documents: List[Dict[str, Any]]):
        upserts = [(doc['id'], embedding) for doc, embedding in zip(documents, embeddings)]
        self.index.upsert(upserts)

    def search(self, query_vector: List[float], top_k: int = 5) -> List[Dict[str, Any]]:
        results = self.index.query(query_vector, top_k=top_k)
        return [match['metadata'] for match in results['matches']]
