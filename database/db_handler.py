import psycopg2

class DBHandler:
    def __init__(self, config):
        self.config = config
        self.connection = None

    def connect(self):
        if self.connection is None:
            self.connection = psycopg2.connect(**self.config)

    def fetch_all(self, query, params=None):
        self.connect()
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()

    def fetch_one(self, query, params=None):
        self.connect()
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchone()

    def execute_query(self, query, params=None):
        self.connect()
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            self.connection.commit()

    def begin_transaction(self):
        self.connect()
        self.connection.autocommit = False

    def commit_transaction(self):
        if self.connection:
            self.connection.commit()
            self.connection.autocommit = True

    def rollback_transaction(self):
        if self.connection:
            self.connection.rollback()
            self.connection.autocommit = True

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None