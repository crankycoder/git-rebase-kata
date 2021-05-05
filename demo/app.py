from flask import Flask
import pytest

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()
