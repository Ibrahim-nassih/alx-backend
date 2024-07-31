#!/usr/bin/env python3
"""Flask app"""
from flask import Flask, request, g, render_template
from flask_babel import Babel
import pytz


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


app.config.from_object('7-app.Config')


@babel.localeselector
def get_locale():
    """get locale"""
    loc = request.args.get('locale', None)
    if loc is not None and loc in app.config['LANGUAGES']:
        return loc
    log = request.args.get("login_as", None)
    if log is not None:
        usr = users[int(log)]['locale']
    if log is not None and usr in app.config["LANGUAGES"]:
        return usr
    if request.headers.get('locale') in app.config['LANGUAGES']:
        return request.headers.get('locale')
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """time zone"""
    loc = request.args.get('timezone', None)
    if loc in pytz.all_timezones:
        return loc
    else:
        raise pytz.exceptions.UnknownTimeZoneError
    log = request.args.get("login_as", None)
    loc = users[int(log)]['timezone']
    if loc in pytz.all_timezones:
        return loc
    else:
        raise pytz.exceptions.UnknownTimeZoneError
    return app.config['BABEL_DEFAULT_TIMEZONE']


def get_user():
    """user"""
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
    return render_template('7-index.html')
