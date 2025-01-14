from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

class DBHandler:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.metadata = MetaData()
        self.metadata.reflect(bind=self.engine, schema='new_schema')
        self.Session = sessionmaker(bind=self.engine)
        print("Available tables:", self.metadata.tables.keys())  # Debug print

    def get_session(self):
        return self.Session()

    def get_table(self, table_name):
        return self.metadata.tables[table_name]