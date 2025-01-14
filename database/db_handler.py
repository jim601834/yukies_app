from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd  # Ensure pandas is imported

class DBHandler:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def get_connection(self):
        return self.engine.connect()

    def get_budget_data(self):
        query = "SELECT * FROM new_schema.budget"
        with self.get_connection() as conn:
            df = pd.read_sql(query, conn)  # Corrected to use pd.read_sql
        return df