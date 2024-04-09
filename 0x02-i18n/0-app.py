#!/usr/bin/env python3
"""
0-app: A basic Flask application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home() -> str:
    """
    Renders the index.html template for the home page.
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
