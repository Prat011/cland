from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

class BaseLLM(ABC):
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        """Generate a response based on the given prompt."""
        pass

    @abstractmethod
    def batch_generate(self, prompts: List[str], **kwargs) -> List[str]:
        """Generate responses for multiple prompts."""
        pass

    @abstractmethod
    def get_num_tokens(self, text: str) -> int:
        """Get the number of tokens in the text."""
        pass
