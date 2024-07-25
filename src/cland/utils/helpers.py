import re
from typing import List, Dict, Any

def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
    """Split text into overlapping chunks."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
    return chunks

def clean_text(text: str) -> str:
    """Clean and normalize text."""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    # Remove special characters
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower()

def merge_dict_lists(dict_lists: List[List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
    """Merge multiple lists of dictionaries, removing duplicates based on 'id'."""
    merged = {}
    for dict_list in dict_lists:
        for item in dict_list:
            if item['id'] not in merged:
                merged[item['id']] = item
    return list(merged.values())
