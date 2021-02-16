from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
from typing import List
import pandas as pds


class CSVIngestor(IngestorInterface):
    '''Ingests quotes from a csv file.
    pandas must be installed on the system.
    '''

    extensions_list = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest '+path)
        quotes = []
        data = pds.read_csv(path)
        for rownum in range(len(data.index)):
            quote = cls.sanitize(data.loc[rownum]['quote'])
            author = cls.sanitize(data.loc[rownum]['author'])
            quotes.append(QuoteModel(quote, author))
        return quotes
