# Software Lab Question Management

A Django coursework application with question management and student/teacher models, using SQLite.

## Requirements

A Python environment compatible with Django 2.2-era APIs. Settings were generated with Django 2.2.12; no requirements file pins the complete environment.

## Getting started

```sh
python -m venv .venv
# Activate .venv and install a compatible Django release.
python manage.py check
python manage.py migrate
python manage.py runserver
```

## Project structure

| Path | Purpose |
| --- | --- |
| `manage.py` | Django management entry point |
| `swlab` | Project settings, URLs, and WSGI |
| `question_manage` | Models, views, migrations, and test module |
| `static` | Static assets |
| `db.sqlite3` | Included development database |

## Configuration and limitations

Use a disposable copy of the included database for development. This legacy Django release is unsupported; dependency modernization is separate from documentation work.

## Development and validation

Run `python manage.py test` in the configured environment and inspect the test count; a generated test module does not guarantee meaningful coverage.

## License

No root-level license file is included. Check source-specific notices and obtain permission before redistribution or reuse.
