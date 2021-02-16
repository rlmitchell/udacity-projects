import os
import time
from PIL import Image, ImageDraw, ImageFont
import random


class MemeEngine:
    def __init__(self, results_dir):
        self.results_dir = self._ensure_dir(results_dir)
        
    def _ensure_dir(self, path):
        try:
            os.mkdir(path, mode=0o700)
        except FileExistsError:
            return path
        except:
            raise

    def _resize_image(self, image, width):
        factor = 1
        if image.width > width:
            factor = round((width/image.width)*100)/100
        return image.resize((int(image.width*factor)-1, int(image.height*factor)-1))

    def _save_image(self, img, path):
        with open(path,'wb') as fout:
            img.save(fout)

    def make_meme(self, img_path: str, body=None, author=None, width=500):
        if not body:  body = 'No Body Supplied'
        if not author:  author = 'No Author Supplied'
        out_path = self.results_dir+'/'+str(time.time()).replace('.','-')+'.jpg'
        fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 10)
        img = Image.open(img_path)
        img = self._resize_image(img, width)
        context = ImageDraw.Draw(img)
        context.text((4,random.randint(4,img.height-8)), f"{body} - {author}", font=fnt, fill="white")
        self._save_image(img, out_path)
        return out_path
