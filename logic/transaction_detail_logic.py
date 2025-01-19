from datetime import datetime
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont
from PySide6.QtWidgets import QHeaderView

class TransactionDetailLogic:
    def __init__(self, db_handler):
        if not db_handler:
            raise ValueError("db_handler is required")
        self.db_handler = db_handler
        self._current_category = None
        self._current_table_views = []

    def load_transaction_detail_data(self, category=None):
        base_query = """
            WITH running_totals AS (
                SELECT 
                    service_date AS date,
                    t_code,
                    to_account AS "to",
                    from__account AS "from",
                    amount::numeric AS amount,
                    CASE 
                        WHEN deduction = 'true' THEN true 
                        ELSE false 
                    END AS tax,
                    SUM(amount::numeric) OVER (
                        ORDER BY service_date ASC, t_code ASC
                    ) AS total
                FROM new_schema.qlog
                WHERE EXTRACT(MONTH FROM service_date) = EXTRACT(MONTH FROM CURRENT_DATE)
                AND EXTRACT(YEAR FROM service_date) = EXTRACT(YEAR FROM CURRENT_DATE)
        """
        
        if category:
            base_query += f" AND category = '{category}'"
        
        query = base_query + """
            )
            SELECT 
                date,
                t_code,
                "to",
                "from",
                amount,
                tax,
                total
            FROM running_totals
            ORDER BY date DESC, t_code DESC
        """
        return self.db_handler.execute_query(query)

    def display_transaction_detail_data(self, df, table_view):
        if df is None or df.empty:
            print("No transaction data to display")
            return

        try:
            table_font = QFont("Arial", 10)
            table_view.setFont(table_font)

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(df.columns)

            header = table_view.horizontalHeader()
            header.setFont(table_font)

            for row in range(df.shape[0]):
                items = []
                for col in range(df.shape[1]):
                    item = QStandardItem()
                    value = df.iloc[row, col]
                    
                    if df.columns[col] in ['amount', 'total']:
                        item.setText(f"${value:,.2f}")
                        item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    elif df.columns[col] == 'tax':
                        item.setText('✓' if bool(value) else '')
                        item.setTextAlignment(Qt.AlignCenter)
                    elif df.columns[col] == 'date':
                        item.setText(value.strftime('%Y-%m-%d'))
                    else:
                        item.setText(str(value))
                    
                    items.append(item)
                
                model.appendRow(items)

            table_view.setModel(model)
            
            for col in range(df.shape[1]):
                if df.columns[col] == 't_code':
                    header.setSectionResizeMode(col, QHeaderView.Interactive)
                    header.resizeSection(col, 80)
                elif df.columns[col] in ['amount', 'total', 'tax']:
                    header.setSectionResizeMode(col, QHeaderView.ResizeToContents)
                else:
                    header.setSectionResizeMode(col, QHeaderView.Stretch)

            table_view.setVisible(True)

        except Exception as e:
            print(f"Error displaying transaction data: {e}")

    def filter_by_category(self, category):
        try:
            print(f"TransactionDetail: Received category filter request: {category}")
            print(f"TransactionDetail: Current registered table views: {len(self._current_table_views)}")
            
            self._current_category = category
            df = self.load_transaction_detail_data(category)
            print(f"TransactionDetail: Loaded {len(df) if df is not None else 0} rows for category {category}")
            
            for table_view in self._current_table_views:
                print(f"TransactionDetail: Updating table view {table_view}")
                self.display_transaction_detail_data(df, table_view)
        except Exception as e:
            print(f"Error filtering by category: {e}")

    def register_table_view(self, table_view):
        if table_view not in self._current_table_views:
            self._current_table_views.append(table_view)
            print(f"TransactionDetail: Registered new table view. Total views: {len(self._current_table_views)}")