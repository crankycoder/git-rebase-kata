import json

from demo import app


def test_index(client):
    response = client.get("/")
    assert response.data == b"Hello, World!"


def test_new_handler(client):
    response = client.get("/fubar")
    assert json.loads(response.data)["status"] == "Situation fubar"


def test_some_crappy_database_write(client):
    response = client.post(
        "/posterboy",
        data=json.dumps(dict(project="foo.bar",)),
        content_type="application/json",
    )

    assert response.status_code == 200
    # TODO: assert that the new row ID is in here
    assert int(json.loads(response.data)["row_id"]) > 0
    print(int(json.loads(response.data)["row_id"]))


def test_get_connection():
    # an undocumented testcase
    memdb_fname = "file::memory:?cache=shared"
    conn = app.create_connection(memdb_fname)
    assert conn is not None
