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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text):
    """return a message"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    """return a number with a message"""
    return "{} is a number".format(n)

if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
