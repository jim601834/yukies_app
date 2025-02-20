from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox, QCheckBox, QSpacerItem, QSizePolicy, QLabel, QDateEdit
from PySide6.QtGui import QDoubleValidator
from PySide6.QtCore import QDate, Signal
from ..logic.data_entry_logic import DataEntryLogic  # Import the DataEntryLogic class

class DataEntryWidget(QWidget):
    submit_data = Signal(dict)  # Custom signal to submit data
    function_button_clicked = Signal(str)  # Signal to communicate function button clicks
    cb1_account_selected = Signal(dict)  # Signal to communicate cb1 account selection
    submit_button_clicked = Signal(dict)  # Signal to communicate submit button click

    def __init__(self, db_handler):
        super().__init__()
        self.logic = DataEntryLogic(db_handler)  # Initialize DataEntryLogic

        # Connect signals
        self.logic.combo_box_data_loaded.connect(self.on_combo_box_data_loaded)
        self.function_button_clicked.connect(self.logic.process_function_button)
        self.cb1_account_selected.connect(self.logic.cb1_account_selected)
        self.submit_button_clicked.connect(self.logic.submit_button_logic)  # Connect submit button signal
        self.logic.tax_checkbox_update.connect(self.update_tax_checkbox)  # Connect tax checkbox update signal

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

        # Spacer between "Date" and "cb1" combo boxes
        spacer2 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        input_layout.addSpacerItem(spacer2)

        # "cb1" combo box
        self.cb1 = QComboBox()
        self.cb1.setEditable(True)
        self.cb1.setFixedWidth(160)
        self.cb1.setFixedHeight(32)
        self.cb1.setEnabled(False)
        self.cb1.setStyleSheet("background-color: lightgray; color: gray;")
        self.cb1.currentIndexChanged.connect(self.on_cb1_account_selected)  # Connect signal
        input_layout.addWidget(self.cb1)

        # Spacer between "cb1" and "cb2" combo boxes
        spacer3 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        input_layout.addSpacerItem(spacer3)

        # "cb2" combo box
        self.cb2 = QComboBox()
        self.cb2.setEditable(True)
        self.cb2.setFixedWidth(160)
        self.cb2.setFixedHeight(32)
        self.cb2.setEnabled(False)
        self.cb2.setStyleSheet("background-color: lightgray; color: gray;")
        input_layout.addWidget(self.cb2)

        # Spacer between "cb2" and "Amount" fields
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
        self.cb1.clear()
        self.cb2.clear()
        self.cb1.lineEdit().setStyleSheet("color: gray")
        self.cb2.lineEdit().setStyleSheet("color: gray")
        self.amount_input.setPlaceholderText("$0000.00")
        self.comment_input.setPlaceholderText("Purpose/Comment")
        self.amount_input.setStyleSheet("background-color: lightgray; color: gray;")
        self.comment_input.setStyleSheet("background-color: lightgray; color: gray;")
        self.amount_input.setEnabled(False)
        self.comment_input.setEnabled(False)

    def enable_combo_boxes_and_inputs(self):
        self.cb1.setEnabled(True)
        self.cb2.setEnabled(True)
        self.amount_input.setEnabled(True)
        self.comment_input.setEnabled(True)
        self.cb1.setStyleSheet("background-color: white; color: black;")
        self.cb2.setStyleSheet("background-color: white; color: black;")
        self.amount_input.setStyleSheet("background-color: white; color: black;")
        self.comment_input.setStyleSheet("background-color: white; color: black;")
        self.cb1.clear()
        self.cb2.clear()

    def on_function_button_clicked(self):
        # Reset the style of the previously active button
        if self.active_button:
            self.active_button.setStyleSheet(self.active_button.default_style)

        # Set the new active button
        self.active_button = self.sender()
        self.active_button.default_style = self.active_button.styleSheet()
        self.active_button.setStyleSheet("background-color: yellow; font-size: 10pt;")

        # Determine t_code based on the button text
        t_code = self.active_button.text().lower()

        # Enable combo boxes and input fields with placeholders
        self.enable_combo_boxes_and_inputs()

        # Emit signal to process function button
        print(f"Emitting signal for function button: {t_code}")
        self.function_button_clicked.emit(t_code)

    def on_cb1_account_selected(self):
        # Emit signal when an account is selected in cb1
        account_name = self.cb1.currentText()
        t_code = self.active_button.text().lower() if self.active_button else ""
        data = {'t_code': t_code, 'account_name': account_name}
        print(f"Emitting signal for cb1 account selected: {data}")
        self.cb1_account_selected.emit(data)

    def on_combo_box_data_loaded(self, to_accounts, from_accounts, cb1_placeholder, cb2_placeholder):
        print("Received signal to load combo box data")
        self.cb1.addItem(cb1_placeholder)
        self.cb2.addItem(cb2_placeholder)
        self.cb1.addItems(sorted(to_accounts))
        self.cb2.addItems(sorted(from_accounts))
        if from_accounts:
            self.cb2.setCurrentText(from_accounts[0])  # Set default value for cb2

    def update_tax_checkbox(self, checked):
        print(f"Updating tax checkbox to: {checked}")
        self.tax_checkbox.setChecked(checked)

    def on_submit_button_clicked(self):
        t_code = self.active_button.text().lower() if self.active_button else ""
        data = {
            't_code': t_code,
            'date': self.date_combo_box.date().toString("yyyy-MM-dd"),
            'cb1': self.cb1.currentText(),
            'cb2': self.cb2.currentText(),
            'amount': self.amount_input.text(),
            'comment': self.comment_input.text(),
            'tax': self.tax_checkbox.isChecked()
        }
        print(f"Emitting submit button clicked signal with data: {data}")  # Add print statement
        self.submit_button_clicked.emit(data)  # Emit the custom signal with the data

        # Reset the style of the active button
        if self.active_button:
            self.active_button.setStyleSheet(self.active_button.default_style)
            self.active_button = None

    def on_reset_button_clicked(self):
        # Reset all input fields and combo boxes
        self.date_combo_box.setDate(QDate.currentDate())
        self.cb1.setCurrentIndex(0)
        self.cb2.setCurrentIndex(0)
        self.amount_input.clear()
        self.comment_input.clear()
        self.tax_checkbox.setChecked(False)

        # Reset the style of the active button
        if self.active_button:
            self.active_button.setStyleSheet(self.active_button.default_style)
            self.active_button = None

        print("Reset button clicked")