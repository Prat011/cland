from typing import List, Dict, Any
from .base import BaseRetriever
from cland.embeddings import BaseEmbedding
from cland.vector_stores import BaseVectorStore

class SemanticSearchRetriever(BaseRetriever):
    def __init__(self, embedding_model: BaseEmbedding, vector_store: BaseVectorStore):
        self.embedding_model = embedding_model
        self.vector_store = vector_store

    def retrieve(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        query_embedding = self.embedding_model.embed_query(query)
        return self.vector_store.search(query_embedding, top_k)
