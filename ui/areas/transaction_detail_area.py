import pandas as pd
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableView
from PySide6.QtCore import Qt, QDate
from database.db_handler import DBHandler  # Correct import path
from logic.utils import create_pandas_model

class TransactionDetailArea(QWidget):
    def __init__(self, db_handler: DBHandler):
        super(TransactionDetailArea, self).__init__()
        self.db_handler = db_handler
        self.layout = QVBoxLayout(self)

        self.heading_label = QLabel("Transaction Detail")
        self.heading_label.setAlignment(Qt.AlignCenter)
        self.heading_label.setStyleSheet("font-size: 8pt; background-color: lightgray")
        self.layout.addWidget(self.heading_label)

        self.table_view = QTableView()
        self.table_view.setStyleSheet("font-size: 8pt")
        self.layout.addWidget(self.table_view)

        self.load_data()

    def load_data(self, category=None):
        current_date = QDate.currentDate()
        current_month = current_date.month()
        current_year = current_date.year()

        if category and category != 'Total':
            query = """
                SELECT 
                    service_date,
                    t_code,
                    to_account,
                    amount,
                    from__account
                FROM new_schema.qlog
                WHERE EXTRACT(MONTH FROM service_date) = %s AND EXTRACT(YEAR FROM service_date) = %s AND category = %s
                ORDER BY service_date DESC
            """
            data = self.db_handler.fetch_all(query, (current_month, current_year, category))
        else:
            query = """
                SELECT 
                    service_date,
                    t_code,
                    to_account,
                    amount,
                    from__account
                FROM new_schema.qlog
                WHERE EXTRACT(MONTH FROM service_date) = %s AND EXTRACT(YEAR FROM service_date) = %s
                ORDER BY service_date DESC
            """
            data = self.db_handler.fetch_all(query, (current_month, current_year))

        columns = ['service_date', 't_code', 'to_account', 'amount', 'from__account']
        df = pd.DataFrame(data, columns=columns)

        # Create a pandas model and set it to the table view
        model = create_pandas_model(df)
        self.table_view.setModel(model)