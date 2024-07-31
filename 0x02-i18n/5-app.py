#!/usr/bin/env python3
"""Flask app"""
from flask import Flask, request, g, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """confige"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('5-app.Config')


@babel.localeselector
def get_locale():
    """get locale"""
    loc = request.args.get('locale', None)
    if loc is not None and loc in app.config['LANGUAGES']:
        return loc
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """get user"""
    log = request.args.get("login_as", None)
    if log is None:
        return None
    return users.get(int(log))


@app.before_request
def before_request():
    """find a user"""
    g.user = get_user()


@app.route('/', strict_slashes=False)
def index():
    """Handles"""
    return render_template('5-index.html')
