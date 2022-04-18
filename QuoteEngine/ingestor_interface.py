from abc import ABC, abstractmethod
"""Importing typing for runtime support for type hints"""
from typing import List

from .quote_model import QuoteModel


class IngestorInterface(ABC):
    """An Abstract base class"""
    file_types = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the file can be ingested"""
        ingest = path.split('.')[-1]
        return ingest in cls.file_types

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
