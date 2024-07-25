from typing import List, Dict, Any
from cland.embeddings import BaseEmbedding
from cland.llms import BaseLLM
from cland.vector_stores import BaseVectorStore
from cland.document_loaders import BaseLoader
from cland.retrievers import BaseRetriever
from cland.prompts import BasePromptTemplate
from cland.utils import chunk_text, clean_text

class RAGToolkit:
    def __init__(
        self,
        embedding_model: BaseEmbedding,
        llm: BaseLLM,
        vector_store: BaseVectorStore,
        document_loader: BaseLoader,
        retriever: BaseRetriever,
        prompt_template: BasePromptTemplate,
        chunk_size: int = 1000,
        chunk_overlap: int = 200
    ):
        self.embedding_model = embedding_model
        self.llm = llm
        self.vector_store = vector_store
        self.document_loader = document_loader
        self.retriever = retriever
        self.prompt_template = prompt_template
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def load_documents(self, source: Any):
        documents = self.document_loader.load(source)
        processed_docs = []
        for doc in documents:
            chunks = chunk_text(doc.page_content, self.chunk_size, self.chunk_overlap)
            for i, chunk in enumerate(chunks):
                processed_docs.append({
                    "id": f"{doc.metadata['source']}_{i}",
                    "text": clean_text(chunk),
                    "metadata": doc.metadata
                })
        
        embeddings = self.embedding_model.embed_documents([doc["text"] for doc in processed_docs])
        self.vector_store.add_embeddings(embeddings, processed_docs)

    def query(self, query: str) -> str:
        cleaned_query = clean_text(query)
        relevant_docs = self.retriever.retrieve(cleaned_query)
        context = "\n".join([doc["text"] for doc in relevant_docs])
        prompt = self.prompt_template.format(query=query, context=context)
        response = self.llm.generate(prompt)
        return response

    def batch_query(self, queries: List[str]) -> List[str]:
        return [self.query(q) for q in queries]

__all__ = ['RAGToolkit']
