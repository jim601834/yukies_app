import pandas as pd
from datetime import datetime

class TransactionDetailLogic:
    def __init__(self, db_handler):
        self.db_handler = db_handler

    def load_transaction_detail_data(self):
        query = """
        SELECT service_date, to_account, amount, from_account
        FROM new_schema.qlog
        WHERE EXTRACT(MONTH FROM service_date) = EXTRACT(MONTH FROM CURRENT_DATE)
        AND EXTRACT(YEAR FROM service_date) = EXTRACT(YEAR FROM CURRENT_DATE)
        """
        df = pd.read_sql(query, self.db_handler.engine)
        df['Total'] = df['amount'].cumsum()
        df = df.rename(columns={
            'service_date': 'Date',
            'to_account': 'To',
            'amount': 'Amount',
            'from_account': 'From'
        })
        return df

    def display_transaction_detail_data(self, df, table_view):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(df.columns)

        for row in df.itertuples(index=False):
            items = [QStandardItem(str(field)) for field in row]
            model.appendRow(items)

        table_view.setModel(model)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)