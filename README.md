# owl

`owl` - is the super minimalistic kn(owl)edge base written in Python with Flask.

App doesn't use a database, all files are stored in plain text in Markdown.

The book is filled in and edited manually on the server. No administrator web-interface is provided.

Full docs and demo: [https://owl.rmrf.space](https://owl.rmrf.space).

## Installation

Install virtualenv:

```
python3 -m venv env
source env/bin/activate
```

Clone repo and install requirements:

```Bash
git clone https://
cd owl
pip install -r requirements.txt
```

Run owl:

```
python3 wsgi.py
```

App is now available at `http://localhost:5000`.

## Usage

By default articles stores at `md/` directory in the same directory where the application is installed. If you want to store articles in a different place, then set this path as the `MD_ROOT` in `config.py`.

Files must have the `.md` extension.

The file name should preferably be without spaces and other characters, except `_` and `-`, since the file name is used in URL.

The `contents.md` contains the content of the book and `home.md` is the home page. Both files are also plain text and requires manual editing.

## License

This software is released under the Unlicense. See [LICENSE.md](LICENSE.md).
