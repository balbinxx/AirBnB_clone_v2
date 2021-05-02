#!/usr/bin/python3
"""Start web app"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def start():
    """Hello"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def another():
    """Return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """return a message"""
    return "C {}".format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
