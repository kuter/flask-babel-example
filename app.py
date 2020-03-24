from flask import Flask, request
from flask_babel import Babel, lazy_gettext

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Choose bet match language from header.

    Returns:
        str: language code

    """
    return request.accept_languages.best_match(['pl', 'en'])


@app.route('/', methods=['POST'])
def index():
    """Translate text.

    Returns:
        str: translated text

    """
    text = request.form['text']
    translated = lazy_gettext(text)
    return str(translated)
