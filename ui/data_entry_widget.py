from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox, QCheckBox, QSpacerItem, QSizePolicy, QLabel, QDateEdit
from PySide6.QtGui import QDoubleValidator
from PySide6.QtCore import QDate

class DataEntryWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # Add a smaller fixed-size spacer at the top
        layout.addSpacerItem(QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed))  # Further reduced height

        # Create a horizontal layout for the input fields
        input_layout = QHBoxLayout()

        # Set fixed height for the input layout
        input_layout.setContentsMargins(0, 0, 0, 0)
        input_layout.setSpacing(5)  # Add space between function buttons

        # "Maintain" button
        self.maintain_button = QPushButton("Maintain")
        self.maintain_button.setStyleSheet("background-color: lightgray; font-size: 10pt;")
        self.maintain_button.setFixedHeight(32)  # Reduced height by 10%
        input_layout.addWidget(self.maintain_button)

        # "Deposit" button
        self.deposit_button = QPushButton("Deposit")
        self.deposit_button.setStyleSheet("background-color: lightblue; font-size: 10pt;")
        self.deposit_button.setFixedHeight(32)  # Reduced height by 10%
        input_layout.addWidget(self.deposit_button)

        # "Withdraw" button
        self.withdraw_button = QPushButton("Withdraw")
        self.withdraw_button.setStyleSheet("background-color: lightblue; font-size: 10pt;")
        self.withdraw_button.setFixedHeight(32)  # Reduced height by 10%
        input_layout.addWidget(self.withdraw_button)

        # "Transfer" button
        self.transfer_button = QPushButton("Transfer")
        self.transfer_button.setStyleSheet("background-color: lightblue; font-size: 10pt;")
        self.transfer_button.setFixedHeight(32)  # Reduced height by 10%
        input_layout.addWidget(self.transfer_button)

        # "Pay" button
        self.pay_button = QPushButton("Pay")
        self.pay_button.setStyleSheet("background-color: lightgreen; font-size: 10pt;")
        self.pay_button.setFixedHeight(32)  # Reduced height by 10%
        input_layout.addWidget(self.pay_button)

        # Spacer between "Pay" and "Date" combo boxes
        spacer1 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        input_layout.addSpacerItem(spacer1)

        # Date combo box
        self.date_combo_box = QDateEdit()
        self.date_combo_box.setCalendarPopup(True)  # Enable calendar popup
        self.date_combo_box.setFixedHeight(32)  # Reduced height
        self.date_combo_box.setStyleSheet("background-color: white;")  # Set background color to white
        self.date_combo_box.setDate(QDate.currentDate())  # Set current date
        input_layout.addWidget(self.date_combo_box)

        # Spacer between "Date" and "To" combo boxes
        spacer2 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        input_layout.addSpacerItem(spacer2)

        # "To" combo box
        self.combo_box_to = QComboBox()
        self.combo_box_to.setEditable(True)  # Make the combo box editable
        self.combo_box_to.setFixedWidth(178)  # Adjust width as needed
        self.combo_box_to.setFixedHeight(32)  # Reduced height
        input_layout.addWidget(self.combo_box_to)

        # Spacer between "To" and "From" combo boxes
        spacer3 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        input_layout.addSpacerItem(spacer3)

        # "From" combo box
        self.combo_box_from = QComboBox()
        self.combo_box_from.setEditable(True)  # Make the combo box editable
        self.combo_box_from.setFixedWidth(181)  # Adjust width as needed
        self.combo_box_from.setFixedHeight(32)  # Reduced height
        input_layout.addWidget(self.combo_box_from)

        # Spacer between "From" and "Amount" fields
        spacer4 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        input_layout.addSpacerItem(spacer4)

        # "Amount" input box
        self.amount_input = QLineEdit()
        self.amount_input.setValidator(QDoubleValidator(0.00, 9999.99, 2))
        self.amount_input.setPlaceholderText("$0000.00")
        self.amount_input.setFixedWidth(80)  # Adjust width as needed
        self.amount_input.setFixedHeight(32)  # Reduced height
        input_layout.addWidget(self.amount_input)

        # Spacer between "Amount" and "Comment" fields
        spacer5 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        input_layout.addSpacerItem(spacer5)

        # "Comment" input box
        self.comment_input = QLineEdit()
        self.comment_input.setPlaceholderText("Purpose/Comment")  # Add placeholder text
        self.comment_input.setFixedWidth(150)  # Increased width
        self.comment_input.setFixedHeight(32)  # Reduced height
        input_layout.addWidget(self.comment_input)

        # Spacer between "Comment" and "Tax" fields
        spacer6 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        input_layout.addSpacerItem(spacer6)

        # "Tax" checkbox and label
        tax_layout = QHBoxLayout()
        self.tax_checkbox = QCheckBox()
        self.tax_checkbox.setFixedHeight(32)  # Reduced height
        tax_layout.addWidget(self.tax_checkbox)
        tax_label = QLabel("Tax")
        tax_label.setContentsMargins(0, 0, 0, 0)  # Move the label closer to the checkbox
        tax_label.setFixedHeight(32)  # Reduced height
        tax_layout.addWidget(tax_label)
        input_layout.addLayout(tax_layout)

        # "Submit" button
        self.submit_button = QPushButton("Submit")
        self.submit_button.setStyleSheet("background-color: lightgreen; font-size: 10pt;")
        self.submit_button.setFixedHeight(32)  # Reduced height by 10%
        input_layout.addWidget(self.submit_button)

        # Add the input layout to the main layout
        layout.addLayout(input_layout)

        # Add a larger vertical spacer at the bottom
        layout.addSpacerItem(QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Expanding))  # Increased height

        # Set fixed height for the entire data entry area
        self.setFixedHeight(5 * 36)  # Approximately the height of 5 lines of text

        # Connect buttons to slots (assuming slots are defined in ComboBoxLogic)
        self.deposit_button.clicked.connect(self.on_deposit_button_clicked)
        self.withdraw_button.clicked.connect(self.on_withdraw_button_clicked)
        self.transfer_button.clicked.connect(self.on_transfer_button_clicked)
        self.pay_button.clicked.connect(self.on_pay_button_clicked)
        self.submit_button.clicked.connect(self.on_submit_button_clicked)

    def populate_date_combo_box(self):
        today = QDate.currentDate()
        self.date_combo_box.setDate(today)

    def set_combo_box_placeholders(self):
        self.combo_box_to.clear()
        self.combo_box_from.clear()
        self.combo_box_to.addItem("Enter To Account")
        self.combo_box_from.addItem("Enter From Account")
        self.combo_box_to.lineEdit().setStyleSheet("color: gray")
        self.combo_box_from.lineEdit().setStyleSheet("color: gray")

    def enable_combo_boxes(self):
        self.combo_box_to.setEnabled(True)
        self.combo_box_from.setEnabled(True)

    def on_deposit_button_clicked(self):
        print("Deposit button clicked")

    def on_withdraw_button_clicked(self):
        print("Withdraw button clicked")

    def on_transfer_button_clicked(self):
        print("Transfer button clicked")

    def on_pay_button_clicked(self):
        print("Pay button clicked")

    def on_submit_button_clicked(self):
        print("Submit button clicked")