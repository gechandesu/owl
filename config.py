class Config(object):
    DEBUG = False
    SECRET_KEY = None
    PASSWORD_FILE = '.pw'
    SIGN_IN = False  # Enable or disable authentication
    MARKDOWN_ROOT = 'docs/'  # Path to your .md files
    MARKDOWN_DOWLOADS = True
    MARKDOWN_EXTRAS = [
        'admonition',
        'attr_list',
        'codehilite',
        'def_list',
        'fenced_code',
        'md_in_html',
        'markdown_alerts',
        'markdown_del_ins',
        'tables',
        'toc'
    ]
    MARKDOWN_EXTRAS_CONFIGS = {
        'markdown_alerts': {
            'info': 'alert alert-info',
            'note': 'alert alert-primary',
            'tip': 'alert alert-success',
            'success': 'alert alert-success',
            'warning': 'alert alert-warning',
            'danger': 'alert alert-danger'
        },
        'toc': {
            'toc_depth': '2-5'
        }
    }