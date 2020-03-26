[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

# Flask-Babel example

## Installation

make sure you have `pipenv` installed:
```
$ pip install pipenv
```

create virtualenv and install requirements:
```
$ pipenv install
```

before you run the command below, make sure that you're in virtualenv:
```
$ pipenv shell
```

## pybabel commnands

collect all messages from python files and generate POT:

```
$ pybabel extract -F translations/babel.cfg -k lazy_gettext -o translations/messages.pot .
```

create directory structure from POT file for given language:

```
$ pybabel init -i translations/messages.pot -d translations/ -l pl
```

update existing message directories:

```
$ pybabel update -i translations/messages.pot -d translations/
```

then compile messages to MO files:

```
$ pybabel compile -d translations
```

## Running project

```
$ flask run
```

## Example usage

```
$ curl -XPOST \
    -F "text=Welcome" \
    -H 'Accept-Language: pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7' \
    localhost:5000
```
