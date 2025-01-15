from datetime import datetime
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont
from PySide6.QtWidgets import QHeaderView

class TransactionDetailLogic:
    def __init__(self, db_handler):
        self.db_handler = db_handler

    def load_transaction_detail_data(self):
        query = """
            WITH running_totals AS (
                SELECT 
                    t_code,
                    service_date AS date,
                    to_account AS to,
                    from__account AS from,
                    amount::numeric AS amount,
                    status AS tax,
                    SUM(amount::numeric) OVER (
                        ORDER BY service_date ASC, t_code ASC
                    ) AS running_total
            FROM new_schema.qlog
            WHERE EXTRACT(MONTH FROM service_date) = EXTRACT(MONTH FROM CURRENT_DATE)
            AND EXTRACT(YEAR FROM service_date) = EXTRACT(YEAR FROM CURRENT_DATE)
        )
        SELECT * FROM running_totals
        ORDER BY date DESC, t_code DESC
        """
        return self.db_handler.execute_query(query)

    def display_transaction_detail_data(self, df, table_view):
        if df is None or df.empty:
            print("No transaction data to display")
            return

        try:
            # Set table font
            table_font = QFont("Arial", 10)
            table_view.setFont(table_font)

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(df.columns)

            # Set header font size
            header = table_view.horizontalHeader()
            header_font = QFont("Arial", 10)
            header.setFont(header_font)

            for row in range(df.shape[0]):
                items = []
                for col in range(df.shape[1]):
                    item = QStandardItem()
                    value = df.iloc[row, col]
                    
                    # Set font size to 10 points
                    font = QFont("Arial", 10)
                    item.setFont(font)
                    
                    if df.columns[col] in ['amount', 'running_total']:
                        item.setText(f"${value:,.2f}")
                        item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    elif df.columns[col] == 'tax':
                        item.setText('✓' if value else '')
                        item.setTextAlignment(Qt.AlignCenter)
                    elif df.columns[col] == 'date':
                        item.setText(value.strftime('%Y-%m-%d'))
                    else:
                        item.setText(str(value))
                    
                    items.append(item)
                
                model.appendRow(items)

            table_view.setModel(model)
            
            header = table_view.horizontalHeader()
            for col in range(df.shape[1]):
                if df.columns[col] == 't_code':
                    header.setSectionResizeMode(col, QHeaderView.Interactive)
                    header.resizeSection(col, 80)  # Set width to 80 pixels (about 6 characters narrower)
                elif df.columns[col] in ['amount', 'running_total', 'tax']:
                    header.setSectionResizeMode(col, QHeaderView.ResizeToContents)
                else:
                    header.setSectionResizeMode(col, QHeaderView.Stretch)

            table_view.setVisible(True)

            print("Model set for table_view")
            print("Table view is visible and resized")
            print(f"Table view is visible: {table_view.isVisible()}")
            print(f"Table view size: {table_view.size()}")
            
            # Debug parent widget visibility
            widget = table_view
            while widget:
                print(f"Parent widget {widget} is visible: {widget.isVisible()}")
                widget = widget.parent()

        except Exception as e:
            print(f"Error displaying transaction data: {e}")