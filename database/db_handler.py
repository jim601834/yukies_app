import psycopg2

class DBHandler:
    def __init__(self, db_config):
        self.connection = psycopg2.connect(**db_config)
        self.cursor = self.connection.cursor()

    def begin_transaction(self):
        self.cursor.execute("BEGIN")

    def commit_transaction(self):
        self.cursor.execute("COMMIT")

    def rollback_transaction(self):
        self.cursor.execute("ROLLBACK")

    def fetch_one(self, query, params):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def fetch_all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def execute_query(self, query, params):
        self.cursor.execute(query, params)