from sqlite3 import Error
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/fubar")
def fubar():
    return jsonify({"status": "Situation fubar"})


@app.route("/posterboy", methods=["POST"])
def posterboy():

    assert isinstance(request.json["project"], str)
    project_name = request.json["project"]

    with create_connection() as conn:
        # create a new project
        create_table(
            conn,
            """
        create table if not exists projects (id integer primary key,
        name  text not null)""",
        )

        sql = """ INSERT INTO projects(name) values (?)"""
        cur = conn.cursor()
        cur.execute(sql, [project_name,])
        conn.commit()
        return jsonify({"row_id": cur.lastrowid})


def create_connection(db_file="file::memory:?cache=shared"):
    # This should be marked private
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
