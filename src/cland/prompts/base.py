from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

class BasePromptTemplate(ABC):
    @abstractmethod
    def format(self, **kwargs) -> str:
        """Format the prompt with the given parameters."""
        pass
