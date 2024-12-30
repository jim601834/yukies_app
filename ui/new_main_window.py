from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QGridLayout, QScrollArea, QWidget
from logic.notifications import send_error_notification
from logic.combo_box_logic import ComboBoxLogic
from database.db_handler import DBHandler
from ui.areas.budget_area import BudgetArea
from ui.areas.transaction_detail_area import TransactionDetailArea
from ui.areas.payment_methods_area import PaymentMethodsArea
from ui.areas.date_range_buttons_area import DateRangeButtonsArea
from ui.data_entry_widget import DataEntryWidget
import pandas as pd
from PySide6.QtCore import QDateTime

class NewMainWindow(QMainWindow):
    def __init__(self):
        super(NewMainWindow, self).__init__()

        # Create the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Set a layout for the central widget
        main_layout = QVBoxLayout(central_widget)

        # Data entry area
        self.data_entry_widget = DataEntryWidget()
        main_layout.addWidget(self.data_entry_widget)

        # Initialize ComboBoxLogic after data_entry_widget is set
        db_config = {
            'dbname': 'yukies_db',
            'user': 'postgres',
            'password': 'sasuke',
            'host': '127.0.0.1',
            'port': '5433'
        }
        self.db_handler = DBHandler(db_config)
        self.combo_box_logic = ComboBoxLogic(self, self.db_handler)

        # Variable to store the title of the button pressed
        self.t_code_holder = None

        # Variable to store the currently displayed category in the transaction detail view
        self.current_category = None

        # Add buttons for Withdraw, Pay, Deposit, and Transfer at the top
        self.withdraw_button = self.data_entry_widget.withdraw_button
        self.pay_button = self.data_entry_widget.pay_button
        self.deposit_button = self.data_entry_widget.deposit_button
        self.transfer_button = self.data_entry_widget.transfer_button

        # Connect buttons to the button_clicked method
        self.withdraw_button.clicked.connect(self.button_clicked)
        self.pay_button.clicked.connect(self.button_clicked)
        self.deposit_button.clicked.connect(self.button_clicked)
        self.transfer_button.clicked.connect(self.button_clicked)

        # Connect the pay_to combo box to the method that checks the category
        self.data_entry_widget.combo_box_to.currentIndexChanged.connect(self.check_category)

        # Scrollable areas in a 2x2 grid
        self.grid_layout = QGridLayout()
        self.budget_area = BudgetArea(self.db_handler)
        self.transaction_detail_area = TransactionDetailArea(self.db_handler)
        self.payment_methods_area = PaymentMethodsArea(self.db_handler)
        self.date_range_buttons_area = DateRangeButtonsArea(self.transaction_detail_area)

        self.add_scroll_area(self.budget_area, 0, 0)
        self.add_scroll_area(self.transaction_detail_area, 0, 1)
        self.add_scroll_area(self.payment_methods_area, 1, 0)
        self.add_scroll_area(self.date_range_buttons_area, 1, 1)

        main_layout.addLayout(self.grid_layout)

        # Maximize the window
        self.showMaximized()

    def add_scroll_area(self, widget, row, col):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(widget)
        self.grid_layout.addWidget(scroll_area, row, col)

    def button_clicked(self):
        # Set the t_code_holder based on the button text
        self.t_code_holder = self.sender().text()
        print(f"{self.t_code_holder} button clicked")

    def check_category(self):
        try:
            to_account = self.data_entry_widget.combo_box_to.currentText()
            if not to_account:
                return

            query = "SELECT acct_category FROM new_schema.top_level_view WHERE acct_name = %s"
            result = self.db_handler.fetch_one(query, (to_account,))
            if result:
                acct_category = result[0]
                if acct_category in ["Medical", "Government"]:
                    self.data_entry_widget.tax_checkbox.setChecked(True)
                else:
                    self.data_entry_widget.tax_checkbox.setChecked(False)
        except Exception as e:
            self.show_error_message(f"An error occurred while checking the category: {e}")

    def on_submit_button_clicked(self):
        try:
            # Capture current date and time
            current_datetime = QDateTime.currentDateTime()
            entry_date = current_datetime.date().toString("yyyy-MM-dd")
            entry_time = current_datetime.time().toString("HH:mm:ss")

            # Capture user inputs
            service_date = self.data_entry_widget.date_list_box.date().toString("yyyy-MM-dd")
            amount = self.data_entry_widget.amount_input.text()
            from_account = self.data_entry_widget.combo_box_from.currentText()
            comment = self.data_entry_widget.comment_box.text()
            deduction = 'true' if self.data_entry_widget.tax_checkbox.isChecked() else 'false'

            # Use the t_code_holder set by the button click
            t_code = self.t_code_holder
            if t_code is None:
                raise ValueError("t_code is not set. Please press a transaction button before submitting.")
            print(f"t_code stored in t_code: {t_code}")

            # Get the to_account and category from the database
            to_account = self.data_entry_widget.combo_box_to.currentText()
            query = "SELECT top_level_name FROM new_schema.top_level_view WHERE acct_name = %s"
            result = self.db_handler.fetch_one(query, (to_account,))
            if result:
                top_level_name = result[0]
                to_account = top_level_name
            else:
                raise ValueError("No matching top_level_name found for the given to_account")

            query = "SELECT acct_distance, acct_category FROM new_schema.accounts WHERE acct_name = %s"
            result = self.db_handler.fetch_one(query, (to_account,))
            if result:
                distance, category = result
            else:
                distance, category = None, None

            # Construct the qlog entry
            qlog_entry = {
                'entry_date': entry_date,
                'entry_time': entry_time,
                'service_date': service_date,
                'amount': amount,
                'from_account': from_account,
                'comment': comment,
                'deduction': deduction,
                't_code': t_code,
                'distance': distance,
                'to_account': to_account,
                'category': category
            }

            # Insert the qlog entry into the database
            query = """
                INSERT INTO new_schema.qlog (entry_date, entry_time, service_date, amount, from__account, "comment", deduction, t_code, distance, to_account, category)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            self.db_handler.execute_query(query, (
                qlog_entry['entry_date'], qlog_entry['entry_time'], qlog_entry['service_date'], qlog_entry['amount'],
                qlog_entry['from_account'], qlog_entry['comment'], qlog_entry['deduction'], qlog_entry['t_code'],
                qlog_entry['distance'], qlog_entry['to_account'], qlog_entry['category']
            ))

            # Reset all data entry fields to their original state
            self.data_entry_widget.date_list_box.setDate(QDate.currentDate())
            self.data_entry_widget.amount_input.clear()
            self.data_entry_widget.combo_box_from.setCurrentIndex(0)
            self.data_entry_widget.comment_box.clear()
            self.data_entry_widget.tax_checkbox.setChecked(False)
            self.data_entry_widget.combo_box_to.setCurrentIndex(0)

            # Reload the budget table to update the values
            self.budget_area.load_data()

            # Reload the transaction detail table to update the values
            self.transaction_detail_area.load_data(self.current_category)

        except Exception as e:
            self.show_error_message(f"An error occurred: {e}")

    def show_error_message(self, message):
        from PySide6.QtWidgets import QMessageBox
        QMessageBox.critical(self, "Error", message)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = NewMainWindow()
    window.show()
    sys.exit(app.exec())