"""
SQLite Handler for Logger

@author: Hideaki Yoshida
"""

import sqlite3
import os

initial_sql_statement = 'CREATE TABLE IF NOT EXISTS log (Log TEXT);'

base_path = os.path.dirname(__file__)
path_to_db = os.path.abspath(os.path.join(base_path, 'logs/log.db'))

def write_log_to_sqlite(log_message):
    connection_to_sqlite = sqlite3.connect(path_to_db)

    with connection_to_sqlite:
        cursor = connection_to_sqlite.cursor()
        cursor.execute(initial_sql_statement)
        try:
            cursor.execute("INSERT INTO log (Log) VALUES (?);", (log_message,))
        except Exception as exception:
            print('Failed to save log into sqlite.')
            print(exception)
            return
        connection_to_sqlite.commit()
