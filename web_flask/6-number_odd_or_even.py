#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask, render_template
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


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """ Displays in /number/<n> route """
    if type(n) == int:
        return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Displays template if n is an int """
    if type(n) == int:
        return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """ Displays template if n is an int """
    if type(n) == int:
        if n % 2 == 0:
            res = "even"
        else:
            res = "odd"
        return render_template("6-number_odd_or_even.html", n=n, res=res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
