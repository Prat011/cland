from typing import Any, Dict, List, Optional
from cland.embeddings.base import BaseEmbedding
from cland.llms.base import BaseLLM
from cland.vector_stores.base import BaseVectorStore
from cland.document_loaders.base import BaseDocumentLoader
from cland.retrievers.base import BaseRetriever
from cland.prompts.base import BasePromptTemplate

class BaseRAG:
    def __init__(
        self,
        embedding_model: BaseEmbedding,
        llm: BaseLLM,
        vector_store: BaseVectorStore,
        document_loader: BaseDocumentLoader,
        retriever: BaseRetriever,
        prompt_template: BasePromptTemplate,
    ):
        self.embedding_model = embedding_model
        self.llm = llm
        self.vector_store = vector_store
        self.document_loader = document_loader
        self.retriever = retriever
        self.prompt_template = prompt_template


    def load_documents(self, source: Any):
        documents = self.document_loader.load(source)
        embeddings = self.embedding_model.embed_documents(documents)
        self.vector_store.add_embeddings(embeddings, documents)

    def query(self, query: str) -> str:
        query_embedding = self.embedding_model.embed_query(query)
        relevant_docs = self.retriever.retrieve(self.vector_store, query_embedding)
        prompt = self.prompt_template.generate(query, relevant_docs)
        response = self.llm.generate(prompt)
        return response

    def update_component(self, component_type: str, new_component: Any):
        if component_type == 'embedding_model':
            self.embedding_model = new_component
        elif component_type == 'llm':
            self.llm = new_component
        elif component_type == 'vector_store':
            self.vector_store = new_component
        elif component_type == 'document_loader':
            self.document_loader = new_component
        elif component_type == 'retriever':
            self.retriever = new_component
        elif component_type == 'prompt_template':
            self.prompt_template = new_component
        else:
            raise ValueError(f"Unknown component type: {component_type}")