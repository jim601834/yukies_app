import pandas as pd
from sqlalchemy import create_engine, text

class DBHandler:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)

    def get_connection(self):
        return self.engine.connect()

    def execute_query(self, query, params=None):
        try:
            with self.get_connection() as connection:
                if params:
                    result = connection.execute(text(query), params)
                else:
                    result = connection.execute(text(query))
                return pd.DataFrame(result.fetchall(), columns=result.keys())
        except Exception as e:
            print(f"Database error: {e}")
            return pd.DataFrame()