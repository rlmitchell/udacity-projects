
__module__ = 'QuoteEngine/quote_model.py'
__version__ = '2020.02.04.1647.rlm'
__info__ = 'Adapted from/for Udemy\'s Python Nanodegree program. '
__student__ = 'Rob Mitchell <rlmitchell@gmail.com>'


class QuoteModel:
    '''Model of a quote:  "quote" - author '''
    def __init__(self, quote, author):
        self.body = quote
        self.author = author

    def __str__(self):
        return (f'"{self.body}" - {self.author}')


'''
Question for reviewer:  Shouldn't this class be named
Quote since it containes a quote and the module file be
named quote_model?  It's not clear to me from the rubric
if the end result is a list of Quote objects or a QuoteModel
object that holds a list of Quotes.

From the comments in @app.route('/') I've chosen to return a list
of QuoteModel objects which are just Quote objects. :)
'''
