from PySide6.QtCore import Signal, QObject, Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont
from PySide6.QtWidgets import QHeaderView

class PaymentMethodsLogicSignals(QObject):
    payment_method_selected = Signal(str)

class PaymentMethodsLogic:
    def __init__(self, db_handler, transaction_detail_logic=None):
        print("\n=== PaymentMethodsLogic Init ===")
        self.db_handler = db_handler
        self.signals = PaymentMethodsLogicSignals()
        self._current_model = None
        
        if transaction_detail_logic:
            print("Connecting payment_method_selected signal")
            try:
                self.signals.payment_method_selected.connect(
                    transaction_detail_logic.filter_by_payment_method
                )
                print("Signal connection successful")
            except Exception as e:
                print(f"ERROR connecting signal: {e}")
                raise
        else:
            print("WARNING: No transaction_detail_logic provided")

    def handle_row_click(self, index):
        print("\n=== Payment Method Row Click ===")
        selected_method = self._current_model.item(index.row(), 0).text()
        print(f"Selected account: {selected_method}")
        print(f"Emitting signal with: {selected_method}")
        self.signals.payment_method_selected.emit(selected_method)
        print("Signal emitted")
        print("=== End Row Click ===\n")

    def load_payment_methods_data(self):
        query = """
            SELECT 
                card_name as "Account",
                statement_balance as "Statement",
                current_balance as "Current",
                monthly_balance as "Monthly",
                closing_date as "Closing",
                payment_date as "Due"
            FROM new_schema.pmt_methods 
            WHERE card_name IS NOT NULL 
            ORDER BY card_name
        """
        return self.db_handler.execute_query(query)

    def display_payment_methods_data(self, df, table_view):
        if df is None or df.empty:
            print("No payment methods data to display")
            return

        table_font = QFont("Arial", 10)
        table_view.setFont(table_font)

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(df.columns)

        header = table_view.horizontalHeader()
        header.setFont(table_font)

        for row in df.itertuples(index=False):
            items = []
            for col, field in enumerate(row):
                item = QStandardItem()
                
                if df.columns[col] in ["Statement", "Current", "Monthly"]:
                    item.setText(f"${field:,.2f}" if field else "$0.00")
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                elif df.columns[col] in ["Closing", "Due"]:
                    item.setText(field.strftime('%Y-%m-%d') if field else "")
                    item.setTextAlignment(Qt.AlignCenter)
                else:
                    item.setText(str(field) if field else "")
                    item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                
                item.setFont(table_font)
                items.append(item)
            
            model.appendRow(items)

        self._current_model = model
        table_view.clicked.connect(self.handle_row_click)
        table_view.setModel(model)

        header.setSectionResizeMode(0, QHeaderView.Interactive)
        header.resizeSection(0, 150)  # Account column
        
        for i in range(1, len(df.columns)):
            if df.columns[i] in ["Statement", "Current", "Monthly"]:
                header.setSectionResizeMode(i, QHeaderView.Interactive)
                header.resizeSection(i, 100)  # Currency columns
            else:
                header.setSectionResizeMode(i, QHeaderView.Interactive)
                header.resizeSection(i, 80)   # Date columns