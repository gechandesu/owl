# owl

![](https://img.shields.io/badge/owl-v1.1-blueviolet)

**owl** — is the minimalistic kn**owl**edge base web app written in Python.

See full docs and demo here: [https://owl.gch.icu/docs/](https://owl.gch.icu/docs/).

Run **owl** in five lines:

```bash
python3 -m venv env
source env/bin/activate
git clone https://github.com/gechandesu/owl.git && cd owl
pip install -r requirements.txt
python owl.py
```

App is now available at [http://localhost:5000/](http://localhost:5000/).

**owl** doesn't use a database, all files are stored in plain text.

This solution is suitable for creating documentation or maintaining a personal knowledge base.

New in `v1.1`:
- Switched to [Python-Markdown](https://github.com/Python-Markdown/markdown).
- Added some new Markdown extensions.

See [CHANGELOG.md](CHANGELOG.md).

# License

This software is licensed under The Unlicense. See [LICENSE](LICENSE).
