from QuoteEngine import TextIngestor, CSVIngestor, PDFIngestor,\
     DocxIngestor, IngestorInterface
from typing import List


__module__ = 'QuoteEngine/ingestor.py'
__version__ = '2020.02.04.1647.rlm'
__info__ = 'Adapted from/for Udemy\'s Python Nanodegree program. '
__student__ = 'Rob Mitchell <rlmitchell@gmail.com>'


class Ingestor(IngestorInterface):
    '''Ingest quotes from multiple file resources.'''

    ingestors = {
        'txt': TextIngestor,
        'csv': CSVIngestor,
        'docx': DocxIngestor,
        'pdf': PDFIngestor
    }

    @classmethod
    def parse(self, quote_files):
        quotes = []
        for quote_file in quote_files:
            ext = quote_file.split('.')[-1]
            quotes.extend(Ingestor.ingestors[ext].parse(quote_file))
        return quotes
