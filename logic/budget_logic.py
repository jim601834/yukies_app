import pandas as pd
from sqlalchemy.orm import sessionmaker
from yukies_app.database.db_handler import DBHandler

class BudgetLogic:
    def __init__(self, db_handler):
        self.db_handler = db_handler
        self.budget_table = self.db_handler.get_table('new_schema.budget')

    def load_budget_data(self, expanded):
        session = self.db_handler.get_session()
        query = session.query(self.budget_table).order_by(self.budget_table.c.display_order)
        df = pd.read_sql(query.statement, self.db_handler.engine)
        print("Loaded data:", df)  # Debug print
        if not expanded:
            df = df[df['display'] == 'Y']
        session.close()
        return df