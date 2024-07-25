from typing import Any, Dict, List, Optional
from cland.embeddings.base import BaseEmbedding
from cland.llms.base import BaseLLM
from cland.vector_stores.base import BaseVectorStore
from cland.document_loaders.base import BaseLoader
from cland.retrievers.base import BaseRetriever
from cland.prompts.base import BasePromptTemplate

class BaseRAG:
    def __init__(
        self,
        embedding_model: BaseEmbedding,
        llm: BaseLLM,
        vector_store: BaseVectorStore,
        document_loader: BaseLoader,
        retriever: BaseRetriever,
        prompt_template: BasePromptTemplate
    ):
        self.embedding_model = embedding_model
        self.llm = llm
        self.vector_store = vector_store
        self.document_loader = document_loader
        self.retriever = retriever
        self.prompt_template = prompt_template

    def load_documents(self, source: Any):
        """Load documents from the specified source and add them to the vector store."""
        documents = self.document_loader.load(source)
        embeddings = self.embedding_model.embed_documents([doc.page_content for doc in documents])
        self.vector_store.add_embeddings(embeddings, documents)

    def query(self, query: str) -> str:
        """Query the RAG system and return a generated response."""
        relevant_docs = self.retriever.retrieve(query)
        context = "\n".join([doc['text'] for doc in relevant_docs])
        prompt = self.prompt_template.format(query=query, context=context)
        response = self.llm.generate(prompt)
        return response

    def update_component(self, component_name: str, new_component: Any):
        """Update a component of the RAG system."""
        if hasattr(self, component_name):
            setattr(self, component_name, new_component)
        else:
            raise ValueError(f"Component {component_name} does not exist in the RAG system.")

class RAGConfig:
    def __init__(self, embedding_model: str, llm_model: str, vector_store_type: str):
        self.embedding_model = embedding_model
        self.llm_model = llm_model
        self.vector_store_type = vector_store_type

    def to_dict(self) -> dict:
        """Convert the configuration to a dictionary."""
        return {
            "embedding_model": self.embedding_model,
            "llm_model": self.llm_model,
            "vector_store_type": self.vector_store_type,
        }
