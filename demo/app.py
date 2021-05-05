from flask import Flask
from flask import jsonify
import pytest

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/fubar")
def fubar():
    return jsonify({"status": "Situation fubar"})


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()
