import os
from typing import List, Optional, Callable
from glob import glob

from cland.document_loaders.base import BaseLoader
from cland import Document
from cland.document_loaders import TextLoader

class DirectoryLoader(BaseLoader):
    """Load documents from a directory."""

    def __init__(
        self,
        path: str,
        glob_pattern: str = "*",
        recursive: bool = True,
        exclude_hidden: bool = True,
        file_extractor: Optional[dict] = None,
    ):
        """Initialize with path to directory.

        Args:
            path (str): Path to directory.
            glob_pattern (str): Glob pattern to match files.
            recursive (bool): Whether to search recursively.
            exclude_hidden (bool): Whether to exclude hidden files.
            file_extractor (Optional[dict]): File extractor to use for each file type.
        """
        self.path = path
        self.glob_pattern = glob_pattern
        self.recursive = recursive
        self.exclude_hidden = exclude_hidden
        self.file_extractor = file_extractor or {}

    def load(self) -> List[Document]:
        """Load documents from directory."""
        docs = []
        search_path = os.path.join(self.path, '**', self.glob_pattern) if self.recursive else os.path.join(self.path, self.glob_pattern)
        
        for file_path in glob(search_path, recursive=self.recursive):
            if self.exclude_hidden and os.path.basename(file_path).startswith('.'):
                continue

            try:
                loader = self._get_loader(file_path)
                docs.extend(loader.load())
            except Exception as e:
                print(f"Error loading file {file_path}: {e}")

        return docs

    def _get_loader(self, file_path: str) -> BaseLoader:
        """Get the appropriate loader for the file type."""
        ext = os.path.splitext(file_path)[-1].lower()
        loader_class = self.file_extractor.get(ext, TextLoader)
        return loader_class(file_path)