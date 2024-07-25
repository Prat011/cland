from typing import List, Dict, Any
from .base import BaseRetriever
from cland.embeddings import BaseEmbedding
from cland.vector_stores import BaseVectorStore

class HybridSearchRetriever(BaseRetriever):
    def __init__(self, embedding_model: BaseEmbedding, vector_store: BaseVectorStore, keyword_weight: float = 0.5):
        self.embedding_model = embedding_model
        self.vector_store = vector_store
        self.keyword_weight = keyword_weight

    def retrieve(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        query_embedding = self.embedding_model.embed_query(query)
        semantic_results = self.vector_store.search(query_embedding, top_k * 2)
        keyword_results = self.vector_store.keyword_search(query, top_k * 2)
        
        # Combine and re-rank results
        combined_results = self._combine_results(semantic_results, keyword_results)
        return combined_results[:top_k]

    def _combine_results(self, semantic_results: List[Dict[str, Any]], keyword_results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        combined = {}
        for i, result in enumerate(semantic_results):
            combined[result['id']] = {'score': (1 - self.keyword_weight) * (1 / (i + 1)), 'data': result}
        for i, result in enumerate(keyword_results):
            if result['id'] in combined:
                combined[result['id']]['score'] += self.keyword_weight * (1 / (i + 1))
            else:
                combined[result['id']] = {'score': self.keyword_weight * (1 / (i + 1)), 'data': result}
        
        return sorted(combined.values(), key=lambda x: x['score'], reverse=True)
