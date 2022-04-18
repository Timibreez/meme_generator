
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
from .csv_ingestor import CsvIngestor
from .docx_ingestor import DocxIngestor
from .pdf_ingestor import PdfIngestor
from .txt_ingestor import TxtIngestor
from typing import List


class Ingestor(IngestorInterface):
    ingestors = [CsvIngestor, DocxIngestor, PdfIngestor, TxtIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Class method parsing file of the path: type."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
