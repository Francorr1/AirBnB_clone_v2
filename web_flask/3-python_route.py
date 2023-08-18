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


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """ Displays in /c/<text> route """
    format_text = text.replace("_", " ")
    return f"C {format_text}"


@app.route("/python/", strict_slashes=False, defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text):
    """ Displays in /python/<text> route """
    format_text = text.replace("_", " ")
    return f"Python {format_text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
