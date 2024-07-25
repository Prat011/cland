from typing import List
import pypdf
from cland import Document
from .base import BaseLoader

class PDFLoader(BaseLoader):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> List[Document]:
        with open(self.file_path, 'rb') as file:
            pdf = pypdf.PdfReader(file)
            documents = []
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                documents.append(Document(page_content=text, metadata={"source": self.file_path, "page": i+1}))
        return documents
