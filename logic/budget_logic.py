
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

        # Set consistent font size
        table_font = QFont("Arial", 10)
        table_view.setFont(table_font)

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(df.columns)

        # Set header font
        header = table_view.horizontalHeader()
        header.setFont(table_font)

        for row in df.itertuples(index=False):
            items = []
            for field in row:
                item = QStandardItem(str(field))
                item.setFont(table_font)
                items.append(item)
            model.appendRow(items)

        # Store model and connect click handler
        self._current_model = model
        table_view.clicked.connect(self.handle_row_click)

        table_view.setModel(model)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table_view.horizontalHeader().resizeSection(0, 200)

    def handle_row_click(self, index):
        # Get clicked category
        category = self._current_model.item(index.row(), 0).text()
        
        # If subcategory, get parent category
        if category.startswith('|---'):
            category = category.split('|---')[1].strip()
            category = category.split(' ')[0]
        
        print(f"Budget: Emitting category_selected signal with category: {category}")
        self.signals.category_selected.emit(category)