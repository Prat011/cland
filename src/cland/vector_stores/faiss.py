import faiss
import numpy as np
from typing import List, Dict, Any
from .base import BaseVectorStore

class FAISSVectorStore(BaseVectorStore):
    def __init__(self):
        self.index = None
        self.documents = []

    def add_embeddings(self, embeddings: List[List[float]], documents: List[Dict[str, Any]]):
        if self.index is None:
            dimension = len(embeddings[0])
            self.index = faiss.IndexFlatL2(dimension)
        
        self.index.add(np.array(embeddings).astype('float32'))
        self.documents.extend(documents)

    def search(self, query_vector: List[float], top_k: int = 5) -> List[Dict[str, Any]]:
        query_vector = np.array(query_vector).reshape(1, -1).astype('float32')
        distances, indices = self.index.search(query_vector, top_k)
        return [self.documents[i] for i in indices[0]]
