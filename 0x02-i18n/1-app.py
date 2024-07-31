#!/usr/bin/env python3
""" Babel setup """
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config(object):
    """configure available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    """return a simple template"""
    return render_template('1-index.html')
