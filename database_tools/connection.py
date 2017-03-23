import psycopg2
import os


# TODO: Fix repetitive code
try:
    DBNAME = os.environ["SFE_DBNAME"]
except KeyError:
    DBNAME = None

try:
    USERNAME = os.environ["SFE_DB_USERNAME"]
except KeyError:
    USERNAME = None

try:
    HOST = os.environ["SFE_DB_HOST"]
except KeyError:
    HOST = None


def get_connection(host=None, dbname=None, username=None):
    """Get a connection. Either read all necessary config from environment variables or provide as parameters.

    :param host: db hostname
    :param dbname: the dataabse name to use
    :param username: the database user name
    :return: A psycopg2 connection object
    :raise: TODO"""

    # TODO: completely untested code
    if all(map(lambda x: x is None, [DBNAME, USERNAME, HOST])):
        assert all(map(lambda x: x is not None, host, dbname, username))
    else:
        assert all(map(lambda x: x is not None, [DBNAME, USERNAME, HOST]))

    conn_statement = "dbname={} user={}".format(DBNAME, USERNAME)
    if HOST is not None:
        conn_statement += " host={}".format(HOST)
    return psycopg2.connect(conn_statement)


def close_connection(connection, cursor):
    """Close the connection. TODO: figure out how to best handle the cursor. Can there exist multiple ones and
    how to make sure they are all properly closed?

    :param connection: A psycopg2 connection
    :param cursor: A psycopg2 cursor
    :return: None
    :raise: TODO"""

    cursor.close()
    connection.close()
