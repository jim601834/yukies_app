import pandas as pd
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QHeaderView

class BudgetLogic:
    def __init__(self, db_handler):
        self.db_handler = db_handler

    def load_budget_data(self, expanded):
        # Load budget data from the database using SQLAlchemy
        query = "SELECT * FROM new_schema.budget"  # Example query
        with self.db_handler.get_connection() as conn:
            df = pd.read_sql(query, conn)
        return df

    def display_budget_data(self, df, table_view):
        # Filter required columns
        df = df[['category', 'amount', 'spent', 'remaining', 'display_order']]
        
        # Sort by display_order
        df = df.sort_values(by='display_order').reset_index(drop=True)
        print("Displaying data:", df)  # Debug print

        # Remove the display_order column for display
        df = df[['category', 'amount', 'spent', 'remaining']]

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(df.columns)

        for row in df.itertuples(index=False):
            items = [QStandardItem(str(field)) for field in row]
            model.appendRow(items)

        print("Setting model for table_view")  # Debug print
        table_view.setModel(model)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Adjust the width of the category column
        category_column_index = df.columns.get_loc('category')
        table_view.horizontalHeader().resizeSection(category_column_index, 200)  # Adjust width as needed

        print("Model set for table_view")  # Debug print

        # Ensure the table view is visible and properly sized
        table_view.setVisible(True)
        table_view.resizeColumnsToContents()
        table_view.resizeRowsToContents()
        print("Table view is visible and resized")  # Debug print

        # Additional debug prints to check the visibility and size of the table view
        print(f"Table view is visible: {table_view.isVisible()}")  # Debug print
        print(f"Table view size: {table_view.size()}")  # Debug print

        # Ensure the table view is explicitly shown
        table_view.show()
        print("Table view explicitly shown")  # Debug print

        # Ensure the parent widgets are visible
        parent_widget = table_view.parentWidget()
        while parent_widget:
            parent_widget.setVisible(True)
            print(f"Parent widget {parent_widget} is visible: {parent_widget.isVisible()}")  # Debug print
            parent_widget = parent_widget.parentWidget()