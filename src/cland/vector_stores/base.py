from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BaseVectorStore(ABC):
    @abstractmethod
    def add_embeddings(self, embeddings: List[List[float]], documents: List[Dict[str, Any]]):
        """Add embeddings and associated documents to the vector store."""
        pass

    @abstractmethod
    def search(self, query_vector: List[float], top_k: int = 5) -> List[Dict[str, Any]]:
        """Search for the top_k documents based on the query vector."""
        pass

    @abstractmethod
    def keyword_search(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """Search for documents containing the given keywords."""
        pass
