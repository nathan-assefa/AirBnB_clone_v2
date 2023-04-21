#!/usr/bin/python3
""" This script starts the wsgi application and the web page
at any ip address of 0.0.0.0 in port 5000
"""
from flask import Flask


apt = Flask(__name__)


@apt.route('/', strict_slashes=False)
def hello():
    """ This function simply rendesrs the string 'Hello HBNB' """
    return ('Hello HBNB!')


@apt.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Rendering a string 'HBNB' """
    return 'HBNB'


@apt.route('/c/<text>', strict_slashes=False)
def text(text):
    """ Rendering a variable and replacign '_' with space """
    text = text.replace('_', ' ')
    return 'C %s' % text


@apt.route('/python/<text>', strict_slashes=False)
def py(text):
    """ Displays the the contents of the variable 'text' """
    text = text.replace('_', ' ')
    if (text):
        return 'Python %s' % text
    else:
        return 'Python text'


if __name__ == "__main__":
    apt.run(host='0.0.0.0', port=5000)
