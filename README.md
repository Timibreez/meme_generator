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
- Activate your virtual environment with <code>pipenv venv/Scripts/activate</code>
- Run `python app.py` or `flask run` on the terminal.
- Follow the link generated.

### Command Line Interface

- Run `python meme.py` on the terminal, and pass the optional CLI arguments below:
  --body: string quote body
  --author: string quote author
  --path: path to image file
  eg: python meme.py --path [PATH to image] --body[BODY] --author[AUTHOR]
