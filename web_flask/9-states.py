#!/usr/bin/python3
""" This script lets the flask app connects to mysql database and
fetch all the data from the states table.

ip address 0.0.0.0 is going to be used to all the machines within the
the network to have access to our app. Port 5000 will be used at entry
point """


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_db(exit):
    """ This context function gives back the
    connection once request is done """
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def db_app(id):
    #this function fetches all the states from mysql database
        s = None
        for state in storage.all(State).values():
            if state.id == id:
                s = state
                break

        return render_template('9-states.html', **locals())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
