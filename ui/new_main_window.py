from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMessageBox, QScrollArea, QLabel, QSizePolicy, QGridLayout
from logic.notifications import send_error_notification
from logic.app_initializer import AppInitializer
from logic.transaction_handler import TransactionHandler
from logic.data_entry_handler import DataEntryHandler
import pandas as pd
from PySide6.QtCore import QDateTime, Qt

class NewMainWindow(QMainWindow):
    def __init__(self):
        super(NewMainWindow, self).__init__()

        # Create the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Set a layout for the central widget
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Create a container for the data entry widget
        data_entry_container = QWidget()
        data_entry_layout = QVBoxLayout(data_entry_container)
        data_entry_layout.setContentsMargins(0, 0, 0, 0)
        data_entry_layout.setSpacing(0)

        # Set fixed height for the container (20% smaller)
        data_entry_container.setFixedHeight(64)  # Adjust the height as needed

        # Data entry area
        from ui.data_entry_widget import DataEntryWidget  # Move import here to avoid circular import
        self.data_entry_widget = DataEntryWidget()
        data_entry_layout.addWidget(self.data_entry_widget)

        # Add the data entry container to the main layout
        main_layout.addWidget(data_entry_container)

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

        # Connect the submit button to the submit method
        self.data_entry_widget.submit_button.clicked.connect(self.on_submit_button_clicked)

        # Connect the function buttons to the button_clicked method
        self.data_entry_widget.maintain_button.clicked.connect(self.button_clicked)
        self.data_entry_widget.withdraw_button.clicked.connect(self.button_clicked)
        self.data_entry_widget.deposit_button.clicked.connect(self.button_clicked)
        self.data_entry_widget.transfer_button.clicked.connect(self.button_clicked)
        self.data_entry_widget.pay_button.clicked.connect(self.button_clicked)

        # Connect the combo box selection change to the method
        self.data_entry_widget.combo_box_to.currentIndexChanged.connect(self.on_combo_box_to_changed)

        # Set initial combo box placeholders
        self.data_entry_widget.set_combo_box_placeholders()

        # Add scrollable areas with content
        self.add_scroll_area(QLabel("Content for Area 1"), 0, 0)
        self.add_scroll_area(QLabel("Content for Area 2"), 0, 1)
        self.add_scroll_area(QLabel("Content for Area 3"), 1, 0)
        self.add_scroll_area(QLabel("Content for Area 4"), 1, 1)

        # Ensure the grid layout stretches to fill the available space
        self.grid_layout.setRowStretch(0, 1)
        self.grid_layout.setRowStretch(1, 1)
        self.grid_layout.setColumnStretch(0, 1)
        self.grid_layout.setColumnStretch(1, 1)

    def add_scroll_area(self, widget, row, col):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(widget)
        scroll_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grid_layout.addWidget(scroll_area, row, col)

    def button_clicked(self):
        # Set the t_code_holder based on the button text
        self.t_code_holder = self.sender().text()
        print(f"{self.t_code_holder} button clicked")

        # Update combo boxes based on the button clicked
        if self.t_code_holder == "Pay":
            self.update_combo_boxes(self.data_entry_handler.load_pay_combo_boxes())
        elif self.t_code_holder == "Transfer":
            self.update_combo_boxes(self.data_entry_handler.load_transfer_combo_boxes())
        elif self.t_code_holder == "Deposit":
            self.update_combo_boxes(self.data_entry_handler.load_deposit_combo_boxes())
        elif self.t_code_holder == "Withdraw":
            self.update_combo_boxes(self.data_entry_handler.load_withdraw_combo_boxes())
        else:
            self.data_entry_widget.set_combo_box_placeholders()
            self.data_entry_widget.enable_combo_boxes()

    def update_combo_boxes(self, accounts):
        try:
            to_accounts, from_accounts = accounts

            # Load the "To" combo box
            self.data_entry_widget.combo_box_to.clear()
            self.data_entry_widget.combo_box_to.addItem("Enter To Account")
            self.data_entry_widget.combo_box_to.lineEdit().setStyleSheet("color: gray")
            for account in to_accounts:
                self.data_entry_widget.combo_box_to.addItem(account[0])

            # Load the "From" combo box
            self.data_entry_widget.combo_box_from.clear()
            self.data_entry_widget.combo_box_from.addItem("Enter From Account")
            self.data_entry_widget.combo_box_from.lineEdit().setStyleSheet("color: gray")
            for account in from_accounts:
                self.data_entry_widget.combo_box_from.addItem(account[0])

            # Enable combo boxes for user input
            self.data_entry_widget.enable_combo_boxes()

        except Exception as e:
            self.show_error_message(f"An error occurred while loading combo boxes: {e}")

    def on_combo_box_to_changed(self):
        if self.t_code_holder == "Pay":
            to_account = self.data_entry_widget.combo_box_to.currentText()
            if to_account and to_account != "Enter To Account":
                self.data_entry_handler.fill_qlog_entry(to_account, self.data_entry_widget, self.t_code_holder)

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
            # Construct the qlog entry
            qlog_entry = self.data_entry_handler.construct_qlog_entry(self.data_entry_widget, self.t_code_holder)

            # Print the qlog entry for now
            print("Qlog Entry:", qlog_entry)

            # Handle the transaction
            self.transaction_handler.handle_transaction(qlog_entry, qlog_entry['from_account'], qlog_entry['to_account'], qlog_entry['amount'])

            # Reinitialize the application
            self.app_initializer.initialize()

        except Exception as e:
            self.show_error_message(f"An error occurred: {e}")

    def show_error_message(self, message):
        QMessageBox.critical(self, "Error", message)

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = NewMainWindow()
    window.showMaximized()  # Ensure the window opens maximized
    sys.exit(app.exec())