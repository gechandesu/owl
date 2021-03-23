import os
import re
from functools import wraps
from datetime import timedelta

import pygments
from markdown2 import Markdown

from flask import Flask
from flask import request
from flask import session
from flask import redirect
from flask import render_template
from flask import send_from_directory
from flask_bcrypt import Bcrypt

from config import Config


app = Flask(__name__)
app.config.from_object(Config)
app.permanent_session_lifetime = timedelta(hours=24)

bcrypt = Bcrypt(app)

def read_file(filepath: str) -> str:
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except IOError:
        return 'Error: Cannot read file: {}'.format(filepath)

def render_html(filepath: str) -> str:
    markdown = Markdown(extras=app.config['MARKDOWN2_EXTRAS'])
    return markdown.convert(
                    read_file(
                        app.config['MARKDOWN_ROOT'] + filepath
                    )
                )

def parse_title_from_markdown(filepath: str) -> str:
    # This function parses article title from first level heading.
    # It returns the occurrence of the first heading, and there
    # can be nothing before it except empty lines and spaces.
    article = read_file(app.config['MARKDOWN_ROOT'] + filepath)
    pattern = re.compile(r'^\s*#\s.*')
    if pattern.search(article):
        return pattern.search(article).group().strip()[2:]
    else:
        return 'Error: Cannot parse title from file:'.format(filepath)

def parse_content_links(filepath: str) -> list:
    # This function returns a list of links from a Markdown file.
    # Only links contained in the list (ul ol li) are parsed.
    r = re.compile(r'(.*(-|\+|\*|\d).?\[.*\])(\(.*\))', re.MULTILINE)
    links = []
    for tpl in r.findall(read_file(app.config['MARKDOWN_ROOT'] + filepath)):
        for item in tpl:
            if re.match(r'\(.*\)', item):
                if item == '(/)':
                    item = '/'  # This is a crutch for fixing the root url
                                # which for some reason continues to contain
                                # parentheses after re.match(r'').
                if not item[1:-1].endswith('/'):
                    item = item[1:-1] + '/'
                links.append(item)
    return links

def check_password(password: str) -> bool:
    if os.path.exists('.pw'):
        pw_hash = read_file('.pw')
        return bcrypt.check_password_hash(pw_hash, password)
    else:
        return False

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.j2'), 404

@app.context_processor
def utility_processor():
    def get_len(list: list) -> int:
        return len(list)
    def get_title(path: str) -> str:
        return parse_title_from_markdown(path[:-1] + '.md')
    return dict(get_title = get_title, get_len = get_len)

def login_required(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if app.config['SIGN_IN']:
            if 'logged_in' in session:
                return func(*args, **kwargs)
            else:
                return redirect('/signin/')
        else:
            return func(*args, **kwargs)
    return wrap

@app.route('/signin/', methods = ['GET', 'POST'])
def signin():
    if request.method == 'POST':
        if check_password(request.form['password']):
            session['logged_in'] = True
            return redirect('/', 302)
        else:
            return render_template('signin.j2', wrong_pw = True)
    else:
        return render_template('signin.j2')

@app.route('/signout/')
@login_required
def signout():
    session.pop('logged_in', None)
    return redirect('/signin/')

@app.route('/')
@login_required
def index():
    return render_template(
        'index.j2',
        title = parse_title_from_markdown('HOME.md'),
        article = render_html('HOME.md'),
        contents = render_html('CONTENTS.md'),
        current_path = '/',
        links = parse_content_links('CONTENTS.md')
    )

@app.route('/<path:path>/')
@login_required
def get_article(path):
    if os.path.exists(app.config['MARKDOWN_ROOT'] + path + '.md'):
        return render_template(
            'index.j2',
            title = parse_title_from_markdown(path + '.md'),
            article = render_html(path + '.md'),
            contents = render_html('CONTENTS.md'),
            current_path = request.path,
            links = parse_content_links('CONTENTS.md')
        )
    else:
        return page_not_found(404)

@app.route('/<path:path>.md')
@login_required
def download_article(path):
    if os.path.exists(app.config['MARKDOWN_ROOT'] + path + '.md') \
    and app.config['MARKDOWN_DOWLOADS']:
        return send_from_directory(
            app.config['MARKDOWN_ROOT'],
            path + '.md'
        )
    else:
        return page_not_found(404)

if __name__ == '__main__':
    app.run()