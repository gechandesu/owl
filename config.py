class Config(object):
    DEBUG = True
    VERSION = '0.1'
    MD_ROOT = 'md/'  # Path to your .md files
    MARKDOWN2_EXTRAS = ['fenced-code-blocks',
                       'code-friendly',
                       'header-ids',
                       'strike',
                       'tables'
                       ]
    # See https://github.com/trentm/python-markdown2/wiki/Extras
