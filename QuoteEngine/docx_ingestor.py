"""Parses docx files creating new quotes"""

import docx
from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class DocxIngestor(IngestorInterface):
    """Parses docx file types and creates quote objects."""

    file_types = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Attempt ingesting the file at path and return QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception("Ingestion failed")

        docx_file = docx.Document(path)
        quote_list = []
        for paragraph in docx_file.paragraphs:
            if paragraph.text != "":
                ingested_text = paragraph.text.split(' - ')
                quote_model = QuoteModel(ingested_text[0], ingested_text[1])
                quote_list.append(quote_model)

        return quote_list
