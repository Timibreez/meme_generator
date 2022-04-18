"""parses csv files, creating new quote objects."""

from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
import pandas as pd


class CsvIngestor(IngestorInterface):
    """Parse csv files and create new quote objects."""

    file_types = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Attempt ingesting the file at path return new QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception("ingestion failed")

        quote_list = []
        data = pd.read_csv(path, header=0, sep=',', error_bad_lines=False)
        for _, row in data.iterrows():
            quote = QuoteModel(row['body'], row['author'])
            quote_list.append(quote)

        return quote_list
