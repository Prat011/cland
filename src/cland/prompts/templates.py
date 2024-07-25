from .base import BasePromptTemplate

class DefaultPromptTemplate(BasePromptTemplate):
    def format(self, query: str, context: str) -> str:
        """Format the prompt for the LLM."""
        return f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
