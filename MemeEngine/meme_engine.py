"""The meme Engine takes an image output file_path,
picks a random image and quote saving the image
to the output file_path returning the file_path of the image."""

import random
from PIL import Image, ImageDraw, ImageFont


class MemeEngine():
    """Takes in an image output file_path,
    selects a random image with a quote,
    saves the image to the output file_path,
    returning the file_path to the image."""

    def __init__(self, output_path):
        """Create instance of class."""
        self.output_path = output_path

    @staticmethod
    def get_rand_y(value):
        """Return a random y-axis value."""
        y_min = 10
        y_max = value-100
        return random.randint(y_min, y_max)

    def make_meme(self, path, text, author, width=500) -> str:
        """Creates meme with a given text and author."""
        try:
            img = Image.open(path)
        except Exception as e:
            print(f'Exception: {e}')
        else:
            if width is not None:
                ratio = width/float(img.size[0])
                height = int(ratio*float(img.size[1]))
                img = img.resize((width, height), Image.Dither.NONE)

            if text and author:
                message = f'{text}\n- {author}'
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype('./font/ZakirahsHand.ttf', 20)
                axis = (10, self.get_rand_y(img.size[1]))
                draw.text(axis, message, font=font, fill='white')

            """Creating the image output file"""
            file_path = f'{self.output_path}/{random.randint(0, 1000000)}.jpeg'

            img.save(file_path)
            print(f'Meme saved {self.output_path}')
            return file_path
