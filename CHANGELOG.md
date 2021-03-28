# Changelog

## v1.1 2021.03.28

### Added

- **owl** switched to `markdown` module.
- `markdown_alerts` extension. Short admonition syntax.
- `markdown_del_ins` extension. Deleted and inserted text support.

### Changed

- Fixed `PASSWORD_FILE` detecting.
- Fixed path resolving. Now uses `os.path.join()`.

### Removed

- `markdown2`. Replaced by `markdown` module.

## v1.0 2021.03.23

### Added

- Bootstrap 5. Brand new frontend.
- Bootstrap Icons.
- `Flask.session` based authentication. Can be enabled in `config.py`. Password encrypted by `bcrypt`.
- `pass.py` to set password.
- Normal 404 error page.
- `CONTENTS.md` parser. You can navigate between articles.
- Article title parser. The title is now displayed in the title of the page.
- New shitcode. It will be refactored in next versions.

### Changed

- `contents.md` and `home.md` renamed to `CONTENTS.md` and `HOME.md`.
- `native` Pygments theme by default.
- File search algorithm changed. Now the viewing of files nested in folders works.
- The main application code has been moved to the `owl.py` module. The launch point of the application is now also the `owl.py`, and not the `wsgi.py`. It may not be the best architectural solution, but it seems to be the most concise now.

### Removed

- Old shitcode removed. See Changed.
- Old frontend and templates.

## v0.1 2020.08.15

First version released.