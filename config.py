class Config(object):
    DEBUG = False
    SECRET_KEY = 'top_secret'
    PASSWORD_FILE = '.pw'
    SIGN_IN = False  # Enable or disable authentication
    MARKDOWN_ROOT = 'docs/'  # Path to your .md files
    MARKDOWN_DOWLOADS = True
    # See https://github.com/trentm/python-markdown2/wiki/Extras
    MARKDOWN2_EXTRAS = [
        'fenced-code-blocks',
        'markdown-in-html',
        'code-friendly',
        'header-ids',
        'strike',
        'tables'
    ]