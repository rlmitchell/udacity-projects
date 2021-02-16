import random
import os
import requests
import time
from flask import Flask, render_template, abort, request
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine
from util.files_list import files_list


app = Flask(__name__)
meme = MemeEngine('./static')


def setup():
    """ Load all resources."""
    quotes_path = "./_data/quotes"
    images_path = "./_data/photos"

    quotes = Ingestor.parse(files_list(quotes_path))
    imgs = files_list(images_path)

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    tmp_path = './static/tmp.'+str(time.time()).replace('.', '-')+'.jpg'
    form = form_dict = request.form.to_dict()
    try:
        img_content = requests.get(form['image_url']).content
    except Exception as e:
        print(e.message, e.args)
        return render_template('meme_form.html')

    with open(tmp_path, 'wb') as img_file:
        img_file.write(img_content)

    try:
        path = meme.make_meme(tmp_path, form['body'], form['author'])
    except Exception as e:
        print(e.message, e.args)
        return render_template('meme_form.html')

    try:
        os.remove(tmp_path)
    except Exception as e:
        print(e.message, e.args)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
