def test_index(client):
    response = client.get("/")
    assert response.data == b"Hello, World!"


def test_new_handler(client):
    response = client.get("/fubar")
    assert response.data == b"Situation fubar"
