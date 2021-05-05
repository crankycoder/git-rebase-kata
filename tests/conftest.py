from demo import app as myapp
import pytest


@pytest.fixture
def app():
    return myapp.app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()
