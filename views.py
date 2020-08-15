from flask import render_template, send_from_directory, request, redirect

from owl import app, get_md_path, render_markdown


@app.before_request
def clear_trailing_slash():
    if request.path != '/' and request.path.endswith('/'):
        return redirect(request.path[:-1])

@app.route('/')
def index():
    return render_template('index.html',
           article = render_markdown(get_md_path()+'home.md'),
           contents = render_markdown(get_md_path()+'contents.md'))

@app.route('/<article_name>')
def get_article(article_name):
    return render_template('index.html',
           article = render_markdown(get_md_path()+article_name+'.md'),
           contents = render_markdown(get_md_path()+'contents.md'))

@app.route('/<article_name>.md')
def download_article(article_name):
    return send_from_directory(get_md_path(), article_name+'.md')
