def test_index(client):
    response = client.get("/")
    assert response.data == b"Hello, World!"


def test_new_handler(client):
    response = client.get("/fubar")
    """
    This should be:

    import json
    assert json.loads(response.data)["status"] == "Situation fubar"

    """
    assert response.data == "Situation fubar"
