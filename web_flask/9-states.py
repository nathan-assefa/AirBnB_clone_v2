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

@app.route('/states', strict_slashes=False)
def states():
    states = list(storage.all().values())
    #states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def cities_of_states(id):
    states = storage.all().values()
    _state = None
    if id:
        for state in states:
            if state.id == id:
                _state = state
                break;

    return render_template('9-states.html', **locals())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
