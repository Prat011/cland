from typing import List, Dict, Any
import qdrant_client
from .base import BaseVectorStore

class QdrantVectorStore(BaseVectorStore):
    def __init__(self, url: str, api_key: str, collection_name: str):
        self.client = qdrant_client.QdrantClient(url, api_key=api_key)
        self.collection_name = collection_name

    def add_embeddings(self, embeddings: List[List[float]], documents: List[Dict[str, Any]]):
        self.client.upsert(
            collection_name=self.collection_name,
            points=[
                qdrant_client.models.PointStruct(
                    id=i,
                    vector=embedding,
                    payload=document
                )
                for i, (embedding, document) in enumerate(zip(embeddings, documents))
            ]
        )

    def search(self, query_vector: List[float], top_k: int = 5) -> List[Dict[str, Any]]:
        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            limit=top_k
        )
        return [hit.payload for hit in results]