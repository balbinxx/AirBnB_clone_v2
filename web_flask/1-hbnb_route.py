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

if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
