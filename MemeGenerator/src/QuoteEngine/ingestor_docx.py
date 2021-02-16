from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
from typing import List
from docx import Document


class DocxIngestor(IngestorInterface):
    '''Ingests quotes from a docx file.'''

    extensions_list = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest '+path)

        quotes = []
        docx = Document(path)
        for paragraph in docx.paragraphs:
            if ' - ' not in paragraph.text:
                continue
            for line in paragraph.text.split('\n'):
                if ' - ' not in line:
                    continue
                quote, author = line.split(' - ')
                quote = cls.sanitize(quote)
                author = cls.sanitize(author)
                quotes.append(QuoteModel(quote, author))
        return quotes
