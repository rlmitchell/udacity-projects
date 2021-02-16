from abc import ABC, abstractmethod
from typing import List
from .quote_model import QuoteModel

__module__ = 'QuoteEngine/ingestor_interface.py'
__version__ = '2020.02.04.1647.rlm'
__info__ = 'Adapted from/for Udemy\'s Python Nanodegree program. '
__student__ = 'Rob Mitchell <rlmitchell@gmail.com>'


class IngestorInterface(ABC):
    '''Interface for ingesting quotes from multiple file resources.'''
    extensions_list = []

    @classmethod
    def sanitize(cls, quote: str) -> str:
        quote = quote.replace('"', '').replace('“', '')
        return quote.replace('”', '').strip()

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return path.split('.')[-1] in cls.extensions_list

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
