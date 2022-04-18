"""Parsing pdf files and creating new quotes."""

import os
import subprocess
import random
from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class PdfIngestor(IngestorInterface):
    """Parses pdf files creating new quotes."""

    file_types = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Ingest Parsed File at path returning QuoteModels."""
        quote_list = []
        if not cls.can_ingest(path):
            raise Exception("Ingestion failed")

        tmp = f'./tmp/{random.randint(0, 10000)}.txt'
        try:
            call = subprocess.call(['pdftotext', path, tmp])
            with open(tmp, 'r') as f:
                contents_of_line = f.readlines()
        except FileNotFoundError as filenotfound:
            print(f'Error: {filenotfound}')
            return quote_list

        for line in contents_of_line:
            line = line.strip('\n\r').strip()
            line_length = len(line)
            if line_length > 0:
                ingested_line = line.split(' - ')
                quote_modell = QuoteModel(ingested_line[0], ingested_line[1])
                quote_list.append(quote_modell)

        f.close()
        os.remove(tmp)
        return quote_list
        