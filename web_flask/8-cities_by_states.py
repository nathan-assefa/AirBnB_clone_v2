#!/usr/bin/python3
""" This script starts the wsgi application and the web page
at any ip address of 0.0.0.0 in port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


# this tear down decorator helps flask to call this method when the query
# + is completed to return all the resources, namely connection, etc
@app.teardown_appcontext
def close_session(exit):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def list_state():
    states = storage.all(State)
    states = [state for state in states.values()]
    return render_template('8-cities_by_states.html', states=states)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
