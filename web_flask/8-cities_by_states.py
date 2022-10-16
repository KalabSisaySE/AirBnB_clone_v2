#!/usr/bin/python3
"""the `8-cities_by_states` module
starts a flask web app
"""

from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def states_list():
    """fetches states and cities and displays it"""
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown():
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
