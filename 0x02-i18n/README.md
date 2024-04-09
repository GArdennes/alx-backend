# 0x02. i18n
## Learning Objectives
1) Learn how to parametrize Flask templates to display different languages
2) Learn how to infer the correct locale based on URL parameters, user settings or request headers
3) Learn how to localize timestamps


## Learning
Flask-Babel is an extension to Flask that adds i18n and I10n support to any Flask application with the help of babel, pytz and speaklater. It has built in support for date formatting with timezone support as well. i18n stands for internationalization, the process of making an app adaptable for different languages while I10n stands for localization and takes an internationalized app and translates its content for a specific language.

#### **Installation**
Here is the code to install the package from PyPi:
`$ pip install Flask-Babel`

#### **Configuration**
You would need to configure your application to follow this pattern
```
from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
# app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)
```

#### **Function: localselector()**
The localselector() language code of the user or request.
```
from flask import Flask, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
def get_locale():
    # 
    return request.accept_languages.best_match(app.config['LANGUAGES'])
```


## Requirements
- All your files will be interpreted on Ubuntu LTS using python3
- All your files should end with a new line
- A readme, file at the root of the folder of the project, is mandatory.
- Your code should use the pycodestyle.
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- All your `*py` files should be executable
- All your modules should have a documentation
- All your classes should have a documentation
- All your functions and methods should have a documentation
- A documentation is not a simple word, it’s a real sentence explaining what the purpose of the module, class or method is.
- All your functions and coroutines must be type-annotated.


## Tasks
### 0. Basic Flask app
First you will setup a basic Flask app in `0-app.py`. Create a single / route and an `index.html` template that simply outputs “Welcome to Holberton” as page title and “Hello world” as header.

### 1. Basic Babel setup
Install the Babel flask extension: `$ pip3 install flask_babel==2.0.0`. Then instantiate the Babel object in your app. Store it in a module-level variable named `babel`. 

In order to configure available languages in our app, you will create a `Config` class that has a `LANGUAGES` class attribute equal to `[“en”, “fr”]`. Use `Config` to set Babel’s default locale (“en”) and timezone (“UTC”).

Use that class as config for your Flask app.

### 2. Get locale from request
Create a `get_locale` function with the `babel.localeselector` decorator. Use `request.accept_languages` to determine the best match with our supported languages.

### 3. Parametrize templates
Use the `_` or `gettext` function to parametrize your templates. Use the message IDs `home_title` and `home_header`. Create a `babel.cfg` file containing
```
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```
Then initialize your translations with `$ pybabel extract -F babel.cfg -o messages.pot .` and your two dictionaries with 
```
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
```
Then edit files `translations/[en | fr]/LC_MESSAGES/messages.po` to provide the correct value for each message ID for each language. Use the following translations:
| msgid              | English                           | French                                   |
| --------------       | -------------------------------  | ------------------------------------- |
| home_title        | “Welcome to Holberton” | “Bienvenue chez Holberton” |
| home_header  | “Hello world!”                  | “Bonjour monde!”                  |

Then compile your dictionaries with `$ pybabel compile -d translations
`. Reload the homepage of your app and make sure that the correct messages show up.

### 4. Force locale with URL parameter
In this task, you will implement a way to force a particular locale by passing the `locale=fr` parameter to your app’s URLs. In your `get_locale` function, detect if the incoming request contains a `locale` argument and if its value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.

Now you should be able to test different translations by visiting `http://127.0.0.1:5000?locale=[fr|en]`.

### 5. Mock logging in
Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in `5-app.py`.
```
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
```
This will mock a database user table. Logging in will be mocked by passing `login_as` URL parameter containing the user ID to log in as. 

Define a `get_user` function that returns a user dictionary or `None` if the ID cannot be found or if ‘login_as’ was not passed.

Define a `before_request` function and use the `app.before_request` decorator to make it executed before all other functions. `before_request` should use `get_user` to find a user if any, and set it as a global on `flask.g.user`.

In your HTML template, if a user is logged in, in a paragraph tag, display a welcome message otherwise display a default message as shown in the table below.

| msgid              | English                                                 | French                                   |
| --------------       | -------------------------------                        | ------------------------------------- |
| logged_in_as   | “You are logged in as %(username)s” | “Vous êtes connecté en tant que %(username)s.” |
| not_logged_in  | “You are not logged in.”                       | “Vous n'êtes pas connecté.”                  |

### 6. Use user locale
Change your `get_locale` function to use a user’s preferred local if it is supported.

The order of priority should be
1. Locale from URL parameters
2. Local from user settings
3. Locale from request header
4. Default locale

Test by logging in as different users

### 7. Infer appropriate time zone
Define a `get_timezone` function and use the `babel.timezoneselector` decorator.

The logic should be the same as `get_locale`:
1. Find `timezone` parameter in URL parameters.
2. Find time zone from user settings.
3. Default to UTC


Before returning a URL-provided or user time zone, you must validate that it is a valid time zone. To that, use pytz.timezone and catch the `pytz.exceptions.UnknownTimeZoneError` exception.

### 8. Display the current time

Based on the inferred time zone, display the current time on the home page in the default format. For example:
`Jan 21, 2020, 5:55:39 AM` or `21 janv. 2020 à 05:56:28`
Use for following translations

| msgid                | English                                                  | French                                        |
| --------------         | -------------------------------                        | -------------------------------------       |
| current_time_is | “The current time is %(current_time)s” | “Nous sommes le %(current_time)s.” |

