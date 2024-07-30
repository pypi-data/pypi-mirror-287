# db_connector_app/__init__.py

"""
db_connector_app

This package provides functionality for connecting to various types of databases including
SQLite, MySQL, PostgreSQL, MongoDB, Cassandra, Redis, CouchDB, DynamoDB, and Neo4j.

Usage:
    from db_connector_app import create_db_connection

    config = {
        'db_type': 'mongodb',
        'db_host': 'localhost',
        'db_port': 27017,
        'db_user': '',
        'db_pass': '',
        'db_name': 'mydatabase'
    }

    connection = create_db_connection(config)
"""

from .connection import create_db_connection
