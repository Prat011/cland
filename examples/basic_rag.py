from cland import (
    BaseRAG,
    FastEmbedEmbedding,
    GeminiLLM,
    QdrantVectorStore,
    WebLoader,
    SemanticSearchRetriever,
    DefaultPromptTemplate
)

# Initialize components
embedding_model = FastEmbedEmbedding()
llm = GeminiLLM(api_key="your_gemini_api_key")
vector_store = QdrantVectorStore(url="your_qdrant_url", api_key="your_qdrant_api_key", collection_name="my_docs")
document_loader = WebLoader()
retriever = SemanticSearchRetriever()
prompt_template = DefaultPromptTemplate()

# Create RAG system
rag = BaseRAG(
    embedding_model=embedding_model,
    llm=llm,
    vector_store=vector_store,
    document_loader=document_loader,
    retriever=retriever,
    prompt_template=prompt_template
)

# Load documents
rag.load_documents("https://example.com/documentation")

# Query the system
response = rag.query("How do I implement feature X?")
print(response)

# Update a component
new_embedding_model = FastEmbedEmbedding(model_name="another-embedding-model")
rag.update_component('embedding_model', new_embedding_model)