
from ingestor_interface import IngestorInterface
from typing import List
from quote_model import QuoteModel
from csv_ingestor import CSVIngestors
from docx_ingestor import DOCXIngestors
from pdf_ingestor import PDFIngestors
from txt_ingestor import TXTIngestors


class Ingestor(IngestorInterface):
    ingestors = [CSVIngestors, DOCXIngestors, PDFIngestors, TXTIngestors]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Class method parsing file of the path: type."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
