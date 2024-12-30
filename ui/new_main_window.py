from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QGridLayout, QScrollArea, QWidget
from logic.notifications import send_error_notification
from ui.data_entry_widget import DataEntryWidget
from logic.app_initializer import AppInitializer
from logic.transaction_handler import TransactionHandler
from logic.data_entry_handler import DataEntryHandler
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

        # Variable to store the title of the button pressed
        self.t_code_holder = None

        # Variable to store the currently displayed category in the transaction detail view
        self.current_category = None

        # Create the grid layout for scrollable areas
        self.grid_layout = QGridLayout()
        main_layout.addLayout(self.grid_layout)

        # Initialize the application
        db_config = {
            'dbname': 'yukies_db',
            'user': 'postgres',
            'password': 'sasuke',
            'host': '127.0.0.1',
            'port': '5433'
        }
        self.app_initializer = AppInitializer(self, db_config)
        self.app_initializer.initialize()

        # Initialize the transaction handler
        self.transaction_handler = TransactionHandler(self.app_initializer.db_handler)

        # Initialize the data entry handler
        self.data_entry_handler = DataEntryHandler(self.app_initializer.db_handler)

        # Maximize the window
        self.showMaximized()

        # Connect the submit button to the submit method
        self.data_entry_widget.submit_button.clicked.connect(self.on_submit_button_clicked)

        # Connect the function buttons to the button_clicked method
        self.data_entry_widget.maintain_button.clicked.connect(self.button_clicked)
        self.data_entry_widget.withdraw_button.clicked.connect(self.button_clicked)
        self.data_entry_widget.deposit_button.clicked.connect(self.button_clicked)
        self.data_entry_widget.transfer_button.clicked.connect(self.button_clicked)
        self.data_entry_widget.pay_button.clicked.connect(self.button_clicked)

        # Set initial combo box placeholders
        self.data_entry_widget.set_combo_box_placeholders()

    def add_scroll_area(self, widget, row, col):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(widget)
        self.grid_layout.addWidget(scroll_area, row, col)

    def button_clicked(self):
        # Set the t_code_holder based on the button text
        self.t_code_holder = self.sender().text()
        print(f"{self.t_code_holder} button clicked")

        # Update combo boxes based on the button clicked
        if self.t_code_holder == "Pay":
            self.load_pay_combo_boxes()
        elif self.t_code_holder == "Transfer":
            self.load_transfer_combo_boxes()
        elif self.t_code_holder == "Deposit":
            self.load_deposit_combo_boxes()
        elif self.t_code_holder == "Withdraw":
            self.load_withdraw_combo_boxes()
        else:
            self.data_entry_widget.set_combo_box_placeholders()
            self.data_entry_widget.enable_combo_boxes()

    def load_pay_combo_boxes(self):
        try:
            pay_to_accounts, pay_from_accounts = self.data_entry_handler.load_pay_combo_boxes()

            # Load the "To" combo box
            self.data_entry_widget.combo_box_to.clear()
            self.data_entry_widget.combo_box_to.addItem("Enter To Account")
            self.data_entry_widget.combo_box_to.lineEdit().setStyleSheet("color: gray")
            for account in pay_to_accounts:
                self.data_entry_widget.combo_box_to.addItem(account[0])

            # Load the "From" combo box
            self.data_entry_widget.combo_box_from.clear()
            self.data_entry_widget.combo_box_from.addItem("Enter From Account")
            self.data_entry_widget.combo_box_from.lineEdit().setStyleSheet("color: gray")
            for account in pay_from_accounts:
                self.data_entry_widget.combo_box_from.addItem(account[0])

            # Enable combo boxes for user input
            self.data_entry_widget.enable_combo_boxes()

        except Exception as e:
            self.show_error_message(f"An error occurred while loading combo boxes: {e}")

    def load_transfer_combo_boxes(self):
        try:
            transfer_to_accounts, transfer_from_accounts = self.data_entry_handler.load_transfer_combo_boxes()

            # Load the "To" combo box
            self.data_entry_widget.combo_box_to.clear()
            self.data_entry_widget.combo_box_to.addItem("Enter To Account")
            self.data_entry_widget.combo_box_to.lineEdit().setStyleSheet("color: gray")
            for account in transfer_to_accounts:
                self.data_entry_widget.combo_box_to.addItem(account[0])

            # Load the "From" combo box
            self.data_entry_widget.combo_box_from.clear()
            self.data_entry_widget.combo_box_from.addItem("Enter From Account")
            self.data_entry_widget.combo_box_from.lineEdit().setStyleSheet("color: gray")
            for account in transfer_from_accounts:
                self.data_entry_widget.combo_box_from.addItem(account[0])

            # Enable combo boxes for user input
            self.data_entry_widget.enable_combo_boxes()

        except Exception as e:
            self.show_error_message(f"An error occurred while loading combo boxes: {e}")

    def load_deposit_combo_boxes(self):
        try:
            deposit_to_accounts, deposit_from_accounts = self.data_entry_handler.load_deposit_combo_boxes()

            # Load the "To" combo box
            self.data_entry_widget.combo_box_to.clear()
            self.data_entry_widget.combo_box_to.addItem("Enter To Account")
            self.data_entry_widget.combo_box_to.lineEdit().setStyleSheet("color: gray")
            for account in deposit_to_accounts:
                self.data_entry_widget.combo_box_to.addItem(account[0])

            # Load the "From" combo box
            self.data_entry_widget.combo_box_from.clear()
            self.data_entry_widget.combo_box_from.addItem("Enter From Account")
            self.data_entry_widget.combo_box_from.lineEdit().setStyleSheet("color: gray")
            for account in deposit_from_accounts:
                self.data_entry_widget.combo_box_from.addItem(account[0])

            # Enable combo boxes for user input
            self.data_entry_widget.enable_combo_boxes()

        except Exception as e:
            self.show_error_message(f"An error occurred while loading combo boxes: {e}")

    def load_withdraw_combo_boxes(self):
        try:
            withdraw_from_accounts = self.data_entry_handler.load_withdraw_combo_boxes()

            # Load the "From" combo box
            self.data_entry_widget.combo_box_from.clear()
            self.data_entry_widget.combo_box_from.addItem("Enter From Account")
            self.data_entry_widget.combo_box_from.lineEdit().setStyleSheet("color: gray")
            for account in withdraw_from_accounts:
                self.data_entry_widget.combo_box_from.addItem(account[0])

            # Set "Cash" in the "To" combo box
            self.data_entry_widget.combo_box_to.clear()
            self.data_entry_widget.combo_box_to.addItem("Cash")
            self.data_entry_widget.combo_box_to.lineEdit().setStyleSheet("color: black")

            # Enable combo boxes for user input
            self.data_entry_widget.enable_combo_boxes()

        except Exception as e:
            self.show_error_message(f"An error occurred while loading combo boxes: {e}")

    def check_category(self):
        try:
            to_account = self.data_entry_widget.combo_box_to.currentText()
            if not to_account:
                return

            query = "SELECT acct_category FROM new_schema.top_level_view WHERE acct_name = %s"
            result = self.app_initializer.db_handler.fetch_one(query, (to_account,))
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
            result = self.app_initializer.db_handler.fetch_one(query, (to_account,))
            if result:
                top_level_name = result[0]
                to_account = top_level_name
            else:
                raise ValueError("No matching top_level_name found for the given to_account")

            query = "SELECT acct_distance, acct_category FROM new_schema.accounts WHERE acct_name = %s"
            result = self.app_initializer.db_handler.fetch_one(query, (to_account,))
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

            # Handle the transaction
            self.transaction_handler.handle_transaction(qlog_entry, from_account, to_account, amount)

            # Reinitialize the application
            self.app_initializer.initialize()

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