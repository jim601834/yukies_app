import pandas as pd
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QHeaderView

class PaymentMethodsLogic:
    def __init__(self, db_handler):
        self.db_handler = db_handler

    def load_payment_methods_data(self):
        # Query to load payment methods data
        query = """
        SELECT card_name AS account, 
               statement_balance AS statement, 
               current_balance AS current, 
               monthly_balance AS monthly, 
               closing_date AS closing, 
               payment_date AS due
        FROM new_schema.pmt_methods  
        """
        with self.db_handler.get_connection() as conn:
            df = pd.read_sql(query, conn)
        return df

    def display_payment_methods_data(self, df, table_view):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(df.columns)

        for row in df.itertuples(index=False):
            items = [QStandardItem(str(field)) for field in row]
            model.appendRow(items)

        table_view.setModel(model)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table_view.setVisible(True)