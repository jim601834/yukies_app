from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox, QCheckBox, QSpacerItem, QSizePolicy, QLabel, QDateEdit
from PySide6.QtGui import QDoubleValidator
from PySide6.QtCore import QDate, Signal

class DataEntryWidget(QWidget):
    submit_data = Signal(dict)  # Custom signal to submit data

    def __init__(self):
        super().__init__()

        # Set background color for the data entry widget
        self.setStyleSheet("background-color: lightgray;")

        layout = QVBoxLayout(self)

        # Adjust the top margin to move everything up by 6 pixels
        layout.setContentsMargins(0, -6, 0, 0)

        # Add a smaller fixed-size spacer at the top
        layout.addSpacerItem(QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Fixed))

        # Create a horizontal layout for the input fields
        input_layout = QHBoxLayout()

        # Set fixed height for the input layout
        input_layout.setContentsMargins(0, 0, 0, 0)
        input_layout.setSpacing(5)

        # Remove "Reset" and "Maintain" buttons
        # "Refund" button
        self.refund_button = QPushButton("Refund")
        self.refund_button.setStyleSheet("background-color: lightcyan; font-size: 10pt;")
        self.refund_button.setFixedHeight(32)
        self.refund_button.setFixedWidth(67)
        input_layout.addWidget(self.refund_button)

        # "Deposit" button
        self.deposit_button = QPushButton("Deposit")
        self.deposit_button.setStyleSheet("background-color: lightblue; font-size: 10pt;")
        self.deposit_button.setFixedHeight(32)
        self.deposit_button.setFixedWidth(67)
        input_layout.addWidget(self.deposit_button)

        # "Withdraw" button
        self.withdraw_button = QPushButton("Withdraw")
        self.withdraw_button.setStyleSheet("background-color: lightblue; font-size: 10pt;")
        self.withdraw_button.setFixedHeight(32)
        self.withdraw_button.setFixedWidth(67)
        input_layout.addWidget(self.withdraw_button)

        # "Transfer" button
        self.transfer_button = QPushButton("Transfer")
        self.transfer_button.setStyleSheet("background-color: lightblue; font-size: 10pt;")
        self.transfer_button.setFixedHeight(32)
        self.transfer_button.setFixedWidth(67)
        input_layout.addWidget(self.transfer_button)

        # "Pay" button
        self.pay_button = QPushButton("Pay")
        self.pay_button.setStyleSheet("background-color: lightgreen; font-size: 10pt;")
        self.pay_button.setFixedHeight(32)
        self.pay_button.setFixedWidth(67)
        input_layout.addWidget(self.pay_button)

        # Spacer between "Pay" and "Date" combo boxes
        spacer1 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        input_layout.addSpacerItem(spacer1)

        # Date combo box
        self.date_combo_box = QDateEdit()
        self.date_combo_box.setCalendarPopup(True)
        self.date_combo_box.setFixedHeight(32)
        self.date_combo_box.setStyleSheet("background-color: white;")
        self.date_combo_box.setDate(QDate.currentDate())
        input_layout.addWidget(self.date_combo_box)

        # Spacer between "Date" and "To" combo boxes
        spacer2 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        input_layout.addSpacerItem(spacer2)

        # "To" combo box
        self.combo_box_to = QComboBox()
        self.combo_box_to.setEditable(True)
        self.combo_box_to.setFixedWidth(160)
        self.combo_box_to.setFixedHeight(32)
        self.combo_box_to.setEnabled(False)
        self.combo_box_to.setStyleSheet("background-color: lightgray; color: gray;")
        input_layout.addWidget(self.combo_box_to)

        # Spacer between "To" and "From" combo boxes
        spacer3 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        input_layout.addSpacerItem(spacer3)

        # "From" combo box
        self.combo_box_from = QComboBox()
        self.combo_box_from.setEditable(True)
        self.combo_box_from.setFixedWidth(160)
        self.combo_box_from.setFixedHeight(32)
        self.combo_box_from.setEnabled(False)
        self.combo_box_from.setStyleSheet("background-color: lightgray; color: gray;")
        input_layout.addWidget(self.combo_box_from)

        # Spacer between "From" and "Amount" fields
        spacer4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        input_layout.addSpacerItem(spacer4)

        # "Amount" input box
        self.amount_input = QLineEdit()
        self.amount_input.setValidator(QDoubleValidator(0.00, 9999.99, 2))
        self.amount_input.setPlaceholderText("$0000.00")
        self.amount_input.setFixedWidth(60)  # Reduced width by 25%
        self.amount_input.setFixedHeight(32)
        self.amount_input.setEnabled(False)
        self.amount_input.setStyleSheet("background-color: lightgray; color: gray;")
        input_layout.addWidget(self.amount_input)

        # Spacer between "Amount" and "Comment" fields
        spacer5 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        input_layout.addSpacerItem(spacer5)

        # "Comment" input box
        self.comment_input = QLineEdit()
        self.comment_input.setPlaceholderText("Purpose/Comment")
        self.comment_input.setFixedWidth(106)  # Reduced width by 25%
        self.comment_input.setFixedHeight(32)
        self.comment_input.setEnabled(False)
        self.comment_input.setStyleSheet("background-color: lightgray; color: gray;")
        input_layout.addWidget(self.comment_input)

        # Spacer between "Comment" and "Tax" fields
        spacer6 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        input_layout.addSpacerItem(spacer6)

        # "Tax" checkbox and label
        tax_layout = QHBoxLayout()
        self.tax_checkbox = QCheckBox()
        self.tax_checkbox.setFixedHeight(32)
        self.tax_checkbox.setStyleSheet("background-color: transparent;")
        tax_layout.addWidget(self.tax_checkbox)
        tax_label = QLabel("Tax")
        tax_label.setContentsMargins(0, 0, 0, 0)
        tax_label.setFixedHeight(32)
        tax_label.setStyleSheet("background-color: transparent;")
        tax_layout.addWidget(tax_label)
        input_layout.addLayout(tax_layout)

        # "Submit" button
        self.submit_button = QPushButton("Submit")
        self.submit_button.setStyleSheet("background-color: lightgreen; font-size: 10pt;")
        self.submit_button.setFixedHeight(32)
        input_layout.addWidget(self.submit_button)

        # Add the input layout to the main layout
        layout.addLayout(input_layout)

        # Add a larger vertical spacer at the bottom
        layout.addSpacerItem(QSpacerItem(20, 45, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Set fixed height for the entire data entry area
        self.setFixedHeight(40)

        # Connect buttons to slots
        self.deposit_button.clicked.connect(self.on_function_button_clicked)
        self.withdraw_button.clicked.connect(self.on_function_button_clicked)
        self.transfer_button.clicked.connect(self.on_function_button_clicked)
        self.pay_button.clicked.connect(self.on_function_button_clicked)
        self.refund_button.clicked.connect(self.on_function_button_clicked)
        self.submit_button.clicked.connect(self.on_submit_button_clicked)

        # Store the currently active button
        self.active_button = None

        # Initialize combo boxes and input fields with placeholders
        self.set_initial_state()

    def set_initial_state(self):
        self.combo_box_to.clear()
        self.combo_box_from.clear()
        self.combo_box_to.addItem("Enter To Account")
        self.combo_box_from.addItem("Enter From Account")
        self.combo_box_to.lineEdit().setStyleSheet("color: gray")
        self.combo_box_from.lineEdit().setStyleSheet("color: gray")
        self.amount_input.setPlaceholderText("$0000.00")
        self.comment_input.setPlaceholderText("Purpose/Comment")
        self.amount_input.setStyleSheet("background-color: lightgray; color: gray;")
        self.comment_input.setStyleSheet("background-color: lightgray; color: gray;")
        self.amount_input.setEnabled(False)
        self.comment_input.setEnabled(False)

    def enable_combo_boxes_and_inputs(self):
        self.combo_box_to.setEnabled(True)
        self.combo_box_from.setEnabled(True)
        self.amount_input.setEnabled(True)
        self.comment_input.setEnabled(True)
        self.combo_box_to.setStyleSheet("background-color: white; color: gray;")
        self.combo_box_from.setStyleSheet("background-color: white; color: gray;")
        self.amount_input.setStyleSheet("background-color: white; color: gray;")
        self.comment_input.setStyleSheet("background-color: white; color: gray;")
        self.combo_box_to.clear()
        self.combo_box_from.clear()
        self.combo_box_to.addItem("Select 'To' Account")
        self.combo_box_from.addItem("Select 'From' Account")
        self.amount_input.setPlaceholderText("1000.00")
        self.comment_input.setPlaceholderText("Purpose/Comment")

    def load_combo_box_data(self, t_code):
        # Placeholder for loading data from the database
        # Replace this with actual database queries to load data into the combo boxes
        to_view = f"{t_code}_to_view"
        from_view = f"{t_code}_from_view"

        # Example data loading (replace with actual database queries)
        to_accounts = self.fetch_data_from_view(to_view)
        from_accounts = self.fetch_data_from_view(from_view)

        self.combo_box_to.addItems(to_accounts)
        self.combo_box_from.addItems(from_accounts)

    def fetch_data_from_view(self, view_name):
        # Placeholder method to fetch data from the database view
        # Replace this with actual database queries
        # Example:
        # query = f"SELECT account_name FROM {view_name}"
        # result = execute_query(query)
        # return [row['account_name'] for row in result]
        return ["Account1", "Account2", "Account3"]  # Example data

    def on_function_button_clicked(self):
        # Reset the style of the previously active button
        if self.active_button:
            self.active_button.setStyleSheet(self.active_button.default_style)

        # Set the new active button
        self.active_button = self.sender()
        self.active_button.default_style = self.active_button.styleSheet()
        self.active_button.setStyleSheet("background-color: yellow; font-size: 10pt;")

        print(f"{self.active_button.text()} button clicked")

        # Determine t_code based on the button text
        t_code = self.active_button.text().lower()

        # Enable combo boxes and input fields with placeholders
        self.enable_combo_boxes_and_inputs()

        # Load combo box data based on t_code
        self.load_combo_box_data(t_code)

    def on_submit_button_clicked(self):
        data = {
            'date': self.date_combo_box.date().toString("yyyy-MM-dd"),
            'to_account': self.combo_box_to.currentText(),
            'from_account': self.combo_box_from.currentText(),
            'amount': self.amount_input.text(),
            'comment': self.comment_input.text(),
            'tax': self.tax_checkbox.isChecked()
        }
        self.submit_data.emit(data)  # Emit the custom signal with the data

        # Reset the style of the active button
        if self.active_button:
            self.active_button.setStyleSheet(self.active_button.default_style)
            self.active_button = None

    def on_reset_button_clicked(self):
        # Reset all input fields and combo boxes
        self.date_combo_box.setDate(QDate.currentDate())
        self.combo_box_to.setCurrentIndex(0)
        self.combo_box_from.setCurrentIndex(0)
        self.amount_input.clear()
        self.comment_input.clear()
        self.tax_checkbox.setChecked(False)

        # Reset the style of the active button
        if self.active_button:
            self.active_button.setStyleSheet(self.active_button.default_style)
            self.active_button = None

        print("Reset button clicked")