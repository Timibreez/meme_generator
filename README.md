# Meme Generator Project

## Overview

Meme Generator an Udacity Intermediate Python Project. Build a python application to generate random memes from user inputs through the command line and web interface. Inputs:
    - quote
    - author
    - image.


## Getting Started

### Flask Web Interface

- Clone the repo <code>git clone https://github.com/Timibreez/meme_generator.git</code>
- Create a virtual environment with <code>python venv 'nameofvirtualenvironment'</code>
- install the dependencies in the requirements.txt file with <code>pipenv install -r requirements.txt</code>
- Activate your virtual environment with <code>pipenv venv/Scripts/activate</code> and Run `python app.py` or `flask run` on the terminal.
- Follow the link generated.

### Command Line Interface

- Run `python meme.py` on the terminal, and pass the optional CLI arguments below:
  --body: string quote body
  --author: string quote author
  --path: path to image file
  eg: python meme.py --path [PATH to image] --body[BODY] --author[AUTHOR]


# Meme Generator Project

## Overview

Meme Generator which is the second project of the Intermediate Python Nanodegree. The task was to build a python application to generate random memes from user inputs through a command line and web interface. The inputs include quote, author, and image.

## Main Modules

- [QuoteEngine](./QuoteEngine)
- [MemeEngine](./MemeEngine)

## Packages

- [Flask](https://github.com/pallets/flask/)
- [Pandas](https://github.com/pandas-dev/pandas)
- [Python-docx](https://github.com/python-openxml/python-docx)
- [Pillow](https://github.com/python-pillow/Pillow)
- [Requests](https://github.com/psf/requests)
- [Subprocess](https://github.com/python/cpython/blob/main/Lib/subprocess.py)
- [ABC](https://github.com/python/cpython/blob/main/Lib/abc.py)
- [Typing](https://github.com/python/typing)
- [os](https://github.com/python/cpython/blob/main/Lib/os.py)
- [Argparse](https://github.com/python/cpython/blob/main/Lib/argparse.py)

## Usage

### Flask Web Interface

- Run `python app.py` on the terminal.
- Access the webpage via this url [http://localhost:5000](http://localhost:5000).

### Command Line Interface

- Run `python meme.py` on the terminal, and pass the optional CLI arguments below:
  --body: string quote body
  --author: string quote author
  --path: path to image file
  Resulting in a command like the following: python meme.py --path [PATH to image] --body[BODY] --author[AUTHOR]

## Submodules Summary

This project is split up into many modules/directories, but the main ones are the [QuoteEngine](./QuoteEngine) and [MemeEngine](./MemeEngine) modules that handle parsing & extracting data from files and later using it to create memes, respectively. The \_data directory holds all the data for various parts of the project. The tmp directory is responsible for keeping temporary files created. The static directory is for static files created when running meme.py/app.py.
