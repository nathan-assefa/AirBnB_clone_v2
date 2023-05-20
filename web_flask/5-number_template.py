#!/usr/bin/python3
""" Writing a script that starts a Flask web app """

from flask import Flask, render_template

# here we create wsgi(web server gateway interface to let the
# flask framework communicate with the web server)
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    return ('Hello HBNB!')

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return ('HBNB')

@app.route('/c/<text>')
def c_text(text):
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)