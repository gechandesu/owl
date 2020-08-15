import os

from flask import Flask
from markdown2 import Markdown
import pygments

from config import Config


app = Flask(__name__)
app.config.from_object(Config)


def get_md_path():
    return os.path.join(app.config['MD_ROOT'])

def render_markdown(filepath):
    """This function renders Markdown file to HTML"""
    markdown = Markdown(extras=app.config['MARKDOWN2_EXTRAS'])

    try:
        with open(filepath, 'r') as md_file:
            return markdown.convert(md_file.read())
    except IOError:
        return '<center><h2>'\
                +os.path.basename(filepath)\
                +': No such file!</h2><center>'

def main():
    print("See https://github.com/gechandesu/owl for info. Whoo!")


if __name__ == "__main__":
    main()
