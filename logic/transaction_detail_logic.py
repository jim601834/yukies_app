from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont
from PySide6.QtWidgets import QHeaderView
from datetime import datetime

class TransactionDetailLogic:
    def __init__(self, db_handler):
        print("\n=== TransactionDetailLogic Init ===")
        self.db_handler = db_handler
        self._current_table_views = []
        self._current_category = None
        self._current_payment_method = None
        self.NO_DATA_MESSAGE = "No transactions found for the selected filter"
        print("Initialization complete")

    def load_transaction_detail_data(self, payment_method=None, category=None):
        print("\n=== Transaction Query ===")
        print(f"Building query with filters:")
        if payment_method:
            print(f"  Payment Method (from__account): '{payment_method}'")
        if category:
            print(f"  Category: '{category}'")
        
        base_query = """
            WITH running_totals AS (
                SELECT 
                    service_date AS date,
                    t_code,
                    to_account AS "to",
                    from__account AS "from",
                    amount::numeric AS amount,
                    SUM(amount::numeric) OVER (
                        ORDER BY service_date ASC, t_code ASC
                    ) AS total,
                    CASE WHEN deduction = 'true' THEN true ELSE false END AS tax
                FROM new_schema.qlog
                WHERE EXTRACT(MONTH FROM service_date) = EXTRACT(MONTH FROM CURRENT_DATE)
                AND EXTRACT(YEAR FROM service_date) = EXTRACT(YEAR FROM CURRENT_DATE)
        """
        
        conditions = []
        if payment_method:
            conditions.append(f"from__account = '{payment_method}'")
            print(f"Added payment filter: from__account = '{payment_method}'")
        elif category and category.lower() != 'total':
            conditions.append(f"category = '{category}'")
            print(f"Added category filter: category = '{category}'")
        
        if conditions:
            base_query += f" AND {' AND '.join(conditions)}"
        
        query = base_query + """
            )
            SELECT 
                date,
                t_code,
                "to",
                "from",
                amount,
                total,
                tax
            FROM running_totals
            ORDER BY date DESC, t_code DESC;
        """
        
        print("Executing query:")
        print(query)
        result = self.db_handler.execute_query(query)
        row_count = len(result) if result is not None else 0
        print(f"Query returned {row_count} rows")
        return result

    def display_transaction_detail_data(self, df, table_view):
        if df is None or df.empty:
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(['Message'])
            item = QStandardItem(self.NO_DATA_MESSAGE)
            item.setFont(QFont("Arial", 10))
            item.setTextAlignment(Qt.AlignCenter)
            model.appendRow([item])
            table_view.setModel(model)
            header = table_view.horizontalHeader()
            header.setSectionResizeMode(0, QHeaderView.Stretch)
            return

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
                    item.setTextAlignment(Qt.AlignCenter)
                else:
                    item.setText(str(value))
                    item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                
                item.setFont(table_font)
                items.append(item)
            
            model.appendRow(items)

        table_view.setModel(model)
        
        header.setSectionResizeMode(0, QHeaderView.Interactive)  # date
        header.resizeSection(0, 100)
        header.setSectionResizeMode(1, QHeaderView.Interactive)  # t_code
        header.resizeSection(1, 80)
        
        for i in range(2, df.shape[1]):
            if df.columns[i] in ['amount', 'total']:
                header.setSectionResizeMode(i, QHeaderView.Interactive)
                header.resizeSection(i, 100)
            elif df.columns[i] == 'tax':
                header.setSectionResizeMode(i, QHeaderView.Interactive)
                header.resizeSection(i, 50)
            else:
                header.setSectionResizeMode(i, QHeaderView.Stretch)

    def filter_by_category(self, category):
        print("\n=== TRANSACTION DETAIL CATEGORY FILTER ===")
        print(f"SIGNAL RECEIVED - Category: '{category}'")
        self._current_category = None if category.lower() == 'total' else category
        print(f"Set category filter to: '{self._current_category}'")
        
        df = self.load_transaction_detail_data(
            category=self._current_category
        )
        print(f"Updating {len(self._current_table_views)} views")
        for view in self._current_table_views:
            self.display_transaction_detail_data(df, view)
        print("=== END CATEGORY FILTER ===\n")

    def filter_by_payment_method(self, payment_method):
        print("\n=== TRANSACTION DETAIL PAYMENT FILTER ===")
        print(f"SIGNAL RECEIVED - Payment Method: '{payment_method}'")
        print(f"Type of payment_method: {type(payment_method)}")
        print(f"Will filter on from__account = '{payment_method}'")
        
        df = self.load_transaction_detail_data(
            payment_method=payment_method
        )
        
        row_count = len(df) if df is not None else 0
        print(f"Query returned {row_count} rows")
        if row_count > 0:
            print("Sample data - First row:")
            print(f"  from__account: {df.iloc[0]['from']}")
            print(f"  amount: ${df.iloc[0]['amount']:,.2f}")
        
        print(f"Updating {len(self._current_table_views)} views")
        for view in self._current_table_views:
            self.display_transaction_detail_data(df, view)
        print("=== END PAYMENT FILTER ===\n")

    def register_table_view(self, table_view):
        if table_view not in self._current_table_views:
            self._current_table_views.append(table_view)
            print(f"Registered new transaction detail view")