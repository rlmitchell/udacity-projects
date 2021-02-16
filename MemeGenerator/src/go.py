import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor

# @TODO Import your Ingestor and MemeEngine classes


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']


    quotes = Ingestor.parse(quote_files)

    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []
    for _file in os.listdir(images_path):
        #if _file.endswith(".txt"):
        print(os.path.join(images_path, _file))
    imgs = None

    return quotes, imgs


quotes, imgs = setup()
