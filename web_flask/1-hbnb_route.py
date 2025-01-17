#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Dislays on web start """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Displays in hbnb route """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
