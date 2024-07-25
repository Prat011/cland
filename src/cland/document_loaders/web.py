from typing import List
import requests
from bs4 import BeautifulSoup
from cland import Document
from .base import BaseLoader

class WebLoader(BaseLoader):
    def __init__(self, url: str):
        self.url = url

    def load(self) -> List[Document]:
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        return [Document(page_content=text, metadata={"source": self.url})]
