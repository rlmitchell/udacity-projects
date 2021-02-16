#!/usr/bin/env python3
"""Command line MeMe generator.

See `README.md` for discussion of this project.
"""


import os
import random
import argparse
import subprocess
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine
from util.files_list import files_list


def fallback_components():
    """Gets substitute image and quote."""
    quotes_path = "./_data/quotes"
    images_path = "./_data/photos"

    quotes = Ingestor.parse(files_list(quotes_path))
    imgs = files_list(images_path)

    return random.choice(quotes), random.choice(imgs)


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote.
    Random substitutes provided if none provided.
    """
    default_quote, default_path = fallback_components()
    img = path = path if path is not None else default_path
    body = body if body is not None else default_quote.body
    author = author if author is not None else default_quote.author

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, body, author)
    return path


def display(path):
    """Wrapper for original print.  Prints the meme file location
    and displays it if possible."""
    print(path)
    if 'linux' in os.sys.platform:
        if 'display' in subprocess.check_output('which display',
                                                shell=True).decode():
            subprocess.run('display '+path, shell=True)


if __name__ == "__main__":
    default_quote, default_path = fallback_components()

    parser = argparse.ArgumentParser(
         description="MeMe Generator CLI"
    )
    parser.add_argument('--path', default=None,
                        help='path to image file')
    parser.add_argument('--body', default=None,
                        help='quote for meme')
    parser.add_argument('--author', default=None,
                        help='author of quote')

    args = parser.parse_args()
    display(generate_meme(args.path, args.body, args.author))
