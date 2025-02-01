import pandas as pd
from sqlalchemy import create_engine, text, Table, Column, Integer, String, Date, DateTime, MetaData
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

class DBHandler:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        self.metadata = MetaData(schema='new_schema')  # Specify the schema
        self.persistent_state = Table(
            'persistent_state', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('state_key', String(255), unique=True, nullable=False),
            Column('state_value', Date),
            Column('last_updated', DateTime)
        )

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

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        session = self.Session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()