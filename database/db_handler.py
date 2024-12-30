import psycopg2
from datetime import datetime, timedelta

class DBHandler:
    def __init__(self, config):
        self.config = config
        self.conn = None
        self.connect()

    def connect(self):
        if self.conn is None or self.conn.closed:
            self.conn = psycopg2.connect(**self.config)

    def close(self):
        if self.conn and not self.conn.closed:
            self.conn.close()

    def execute_query(self, query, params=None):
        self.connect()
        with self.conn.cursor() as cursor:
            cursor.execute(query, params)
            self.conn.commit()

    def fetch_all(self, query, params=None):
        self.connect()
        with self.conn.cursor() as cursor:
            cursor.execute(query, params)
            results = cursor.fetchall()
        return results

    def fetch_one(self, query, params=None):
        self.connect()
        with self.conn.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchone()
        return result

    def get_view_data(self, schema_name, view_name, column_name):
        query = f"SELECT {column_name} FROM {schema_name}.{view_name}"
        return [row[0] for row in self.fetch_all(query)]