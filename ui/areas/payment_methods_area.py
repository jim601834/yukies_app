import pandas as pd
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableView
from PySide6.QtCore import Qt
from database.db_handler import DBHandler
from logic.utils import create_pandas_model

class PaymentMethodsArea(QWidget):
    def __init__(self, db_handler: DBHandler):
        super(PaymentMethodsArea, self).__init__()
        self.db_handler = db_handler
        self.layout = QVBoxLayout(self)

        self.heading_label = QLabel("Payment Methods")
        self.heading_label.setAlignment(Qt.AlignCenter)
        self.heading_label.setStyleSheet("font-size: 8pt; background-color: lightgray")
        self.layout.addWidget(self.heading_label)

        self.table_view = QTableView()
        self.table_view.setStyleSheet("font-size: 8pt")
        self.layout.addWidget(self.table_view)

        self.load_data()

    def load_data(self):
        query = """
            SELECT 
                card_name,
                statement_balance,
                current_balance,
                monthly_balance,
                closing_date,
                payment_date,
                "Type"
            FROM new_schema.pmt_methods
        """
        data = self.db_handler.fetch_all(query)
        columns = ['Card Name', 'Statement', 'Current', 'Monthly', 'Closing', 'Payment', 'Type']
        df = pd.DataFrame(data, columns=columns)

        # Create a pandas model and set it to the table view
        model = create_pandas_model(df)
        self.table_view.setModel(model)

        # Adjust column widths
        self.table_view.setColumnWidth(0, 100)  # Card Name (narrower by about 8 letters)
        self.table_view.setColumnWidth(1, 60)   # Statement (narrower by 4-6 characters)
        self.table_view.setColumnWidth(2, 60)   # Current (narrower by 4-6 characters)
        self.table_view.setColumnWidth(3, 60)   # Monthly (narrower by 4-6 characters)
        self.table_view.setColumnWidth(4, 60)   # Closing (narrower by 4-6 characters)
        self.table_view.setColumnWidth(5, 60)   # Payment (narrower by 4-6 characters)
        self.table_view.setColumnWidth(6, 30)   # Type (already narrow)