from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
from typing import List
import subprocess


class PDFIngestor(IngestorInterface):
    '''Ingests quotes from a pdf file.
    pdftotext must be installed on the system.
    '''
    extensions_list = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        assert 'pdftotext' in \
            subprocess.check_output(['which', 'pdftotext']).decode()
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest '+path)

        quotes = []
        process_output = subprocess.run(['pdftotext', path, '-'],
                                        stdout=subprocess.PIPE)
        for line in process_output.stdout.decode().split('\n'):
            if ' - ' not in line:
                continue
            quote, author = line.split(' - ')
            quote = cls.sanitize(quote)
            author = cls.sanitize(author)
            quotes.append(QuoteModel(quote, author))
        return quotes


'''
Note to reviewer:  This is better done by capturing the pdftotext
output rather than going to disk.  Obviously if that needs to be
demonstrated as a requirement I'll redo it :)
'''
