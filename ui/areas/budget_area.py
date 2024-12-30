import pandas as pd
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableView
from PySide6.QtCore import Qt
from database.db_handler import DBHandler
from logic.utils import create_pandas_model

class BudgetArea(QWidget):
    def __init__(self, db_handler: DBHandler):
        super(BudgetArea, self).__init__()
        self.db_handler = db_handler
        self.layout = QVBoxLayout(self)

        self.heading_label = QLabel("Budget")
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
                category,
                SUM(amount) AS budget,
                SUM(spent) AS spent,
                SUM(remaining) AS remaining
            FROM new_schema.budget
            GROUP BY category
        """
        data = self.db_handler.fetch_all(query)
        columns = ['category', 'budget', 'spent', 'remaining']
        df = pd.DataFrame(data, columns=columns)

        # Perform any necessary calculations
        df['remaining'] = df['budget'] - df['spent']
        df['remaining'] = df['remaining'].round(2)

        # Create a pandas model and set it to the table view
        model = create_pandas_model(df)
        self.table_view.setModel(model)