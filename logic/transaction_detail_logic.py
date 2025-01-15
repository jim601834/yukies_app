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
                    service_date AS date,
                    t_code,
                    to_account AS to,
                    from__account AS from,
                    amount::numeric AS amount,
                    CASE 
                        WHEN deduction = 'true' THEN true 
                        ELSE false 
                    END AS tax,
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
            print("Setting model for table_view")
            
            # Set table font
            table_font = QFont("Arial", 10)
            table_view.setFont(table_font)

            # Create and populate model
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(df.columns)

            # Set header font
            header = table_view.horizontalHeader()
            header.setFont(table_font)

            # Populate data
            for row in range(df.shape[0]):
                items = []
                for col in range(df.shape[1]):
                    item = QStandardItem()
                    value = df.iloc[row, col]
                    
                    if df.columns[col] in ['amount', 'running_total']:
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

            # Set model and configure display
            table_view.setModel(model)
            print("Model set for table_view")
            
            # Configure columns
            for col in range(df.shape[1]):
                if df.columns[col] == 't_code':
                    header.setSectionResizeMode(col, QHeaderView.Interactive)
                    header.resizeSection(col, 80)
                elif df.columns[col] in ['amount', 'running_total', 'tax']:
                    header.setSectionResizeMode(col, QHeaderView.ResizeToContents)
                else:
                    header.setSectionResizeMode(col, QHeaderView.Stretch)

            # Ensure visibility
            table_view.setVisible(True)
            parent = table_view.parent()
            while parent:
                parent.setVisible(True)
                parent = parent.parent()

            print("Table view visibility set")

        except Exception as e:
            print(f"Error displaying transaction data: {e}")