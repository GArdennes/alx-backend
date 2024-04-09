#!/usr/bin/env python3
"""
app: A basic Flask application
"""
import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Configuration class for your Flask application."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    Retrieves a user based on a user id.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """
    Performs some routines before each request's resolution.
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """
    Determines the user's preferred locale based on their browser settings
    """
    header_locale = request.headers.get('locale')
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def validate_timezone(str: timezone) -> str:
    """
    Validate timezone
    """
    try:
        pytz.timezone(timezone)
        return timezone
    except pytz.exceptions.UnknownTimeZoneError:
        return None


@babel.timezoneselector
def get_timezone() -> str:
    """
    Determines the user's preferred timezone based on their settings.
    """
    timezone = request.args.get('timezone')
    if timezone and validate_timezone(timezone):
        return timezone
    if g.user and g.user['timezone'] and validate_timezone(g.user['timezone']):
        return g.user['timezone']
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/', strict_slashes=False)
def home() -> str:
    """
    Renders the index.html template for the home page.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
