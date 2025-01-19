import pandas as pd
from PySide6.QtCore import Signal, QObject
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont
from PySide6.QtWidgets import QHeaderView

class BudgetLogicSignals(QObject):
    category_selected = Signal(str)

class BudgetLogic:
    def __init__(self, db_handler, transaction_detail_logic=None):
        self.db_handler = db_handler
        self.signals = BudgetLogicSignals()
        self._current_model = None
        if transaction_detail_logic:
            self.signals.category_selected.connect(transaction_detail_logic.filter_by_category)

    def load_budget_data(self, expanded):
        query = "SELECT * FROM new_schema.budget"
        with self.db_handler.get_connection() as conn:
            df = pd.read_sql(query, conn)
        return df

    def display_budget_data(self, df, table_view):
        # Filter and sort data
        df = df[['category', 'amount', 'spent', 'remaining', 'display_order']]
        df = df.sort_values(by='display_order').reset_index(drop=True)
        df = df[['category', 'amount', 'spent', 'remaining']]

        # Set table font
        table_font = QFont("Arial", 10)
        table_view.setFont(table_font)

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(df.columns)

        # Set header font
        header = table_view.horizontalHeader()
        header.setFont(table_font)

        # Populate table with data
        for row in df.itertuples(index=False):
            items = []
            for field in row:
                item = QStandardItem(str(field))
                item.setFont(table_font)
                items.append(item)
            model.appendRow(items)

        # Store model reference and connect click handler
        self._current_model = model
        table_view.clicked.connect(self.handle_row_click)

        table_view.setModel(model)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Set column widths
        category_column_index = df.columns.get_loc('category')
        table_view.horizontalHeader().resizeSection(category_column_index, 200)

        # Ensure visibility
        table_view.setVisible(True)
        table_view.resizeColumnsToContents()
        table_view.resizeRowsToContents()
        table_view.show()

        # Ensure parent visibility
        parent_widget = table_view.parentWidget()
        while parent_widget:
            parent_widget.setVisible(True)
            parent_widget = parent_widget.parentWidget()

    def handle_row_click(self, index):
        category = self._current_model.item(index.row(), 0).text()
        self.signals.category_selected.emit(category)