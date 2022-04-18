"""Parses txt files and creates new quotes."""

from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class TxtIngestor(IngestorInterface):
    """Parses txt files, creating new quote."""

    file_types = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Attemps ingesting file, returning a QuoteModel object."""
        if not cls.can_ingest(path):
            raise Exception('Ingestion failed')

        quote_list = []

        with open(path, 'r') as file:
            for line in file.readlines():
                line = line.strip('\n\r').strip()
                line_length = len(line)
                if line_length > 0:
                    parsed_line = line.split(' - ')
                    quote_model = QuoteModel(parsed_line[0], parsed_line[1])
                    quote_list.append(quote_model)

        return quote_list
