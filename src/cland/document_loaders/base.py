from typing import List
from cland import Document
from .base import BaseLoader

class TextLoader(BaseLoader):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> List[Document]:
        with open(self.file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return [Document(page_content=content, metadata={"source": self.file_path})]