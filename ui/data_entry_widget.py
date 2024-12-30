from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QLineEdit, QCheckBox, QLabel, QDateEdit, QSpacerItem, QSizePolicy
from PySide6.QtCore import QDate

class DataEntryWidget(QWidget):
    def __init__(self):
        super(DataEntryWidget, self).__init__()

        # Main layout
        main_layout = QVBoxLayout(self)

        # Data entry layout
        data_entry_layout = QHBoxLayout()

        # Buttons
        self.maintain_button = QPushButton("Maintain")
        self.withdraw_button = QPushButton("Withdraw")
        self.deposit_button = QPushButton("Deposit")
        self.transfer_button = QPushButton("Transfer")
        self.pay_button = QPushButton("Pay")

        # Increase button height and set styles
        button_height = 35
        self.maintain_button.setFixedHeight(button_height)
        self.withdraw_button.setFixedHeight(button_height)
        self.deposit_button.setFixedHeight(button_height)
        self.transfer_button.setFixedHeight(button_height)
        self.pay_button.setFixedHeight(button_height)

        self.maintain_button.setStyleSheet("background-color: lightgray")
        self.withdraw_button.setStyleSheet("background-color: lightblue")
        self.deposit_button.setStyleSheet("background-color: lightblue")
        self.transfer_button.setStyleSheet("background-color: lightblue")
        self.pay_button.setStyleSheet("background-color: lightgreen")

        data_entry_layout.addWidget(self.maintain_button)
        data_entry_layout.addWidget(self.withdraw_button)
        data_entry_layout.addWidget(self.deposit_button)
        data_entry_layout.addWidget(self.transfer_button)
        data_entry_layout.addWidget(self.pay_button)

        # Date list box
        self.date_list_box = QDateEdit()
        self.date_list_box.setCalendarPopup(True)
        self.date_list_box.setDate(QDate.currentDate())
        self.date_list_box.setDisplayFormat("yyyy-MM-dd")
        self.date_list_box.setFixedWidth(110)  # Adjust width to be a couple of characters wider
        data_entry_layout.addWidget(self.date_list_box)

        # Combo boxes
        self.combo_box_to = QComboBox()
        self.combo_box_from = QComboBox()
        self.combo_box_to.setFixedWidth(170)  # Adjust width to be 5 characters wider
        self.combo_box_from.setFixedWidth(170)  # Adjust width to be 5 characters wider
        data_entry_layout.addWidget(self.combo_box_to)

        # Spacer to separate the combo boxes
        spacer_between_combos = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        data_entry_layout.addSpacerItem(spacer_between_combos)

        data_entry_layout.addWidget(self.combo_box_from)

        # Amount input box with placeholder
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("10,000.00")
        self.amount_input.setFixedWidth(80)  # Adjust width to be 6 characters narrower
        data_entry_layout.addWidget(self.amount_input)

        # Spacer to move the comment box to the right
        spacer_before_comment = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        data_entry_layout.addSpacerItem(spacer_before_comment)

        # Comment box
        self.comment_box = QLineEdit()
        self.comment_box.setPlaceholderText("Comment/Purpose")
        self.comment_box.setFixedWidth(110)  # Adjust width to be 10 characters narrower
        data_entry_layout.addWidget(self.comment_box)

        # Spacer to move the checkbox to the right
        spacer_before_checkbox = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        data_entry_layout.addSpacerItem(spacer_before_checkbox)

        # Tax checkbox
        self.tax_checkbox = QCheckBox("Tax")
        data_entry_layout.addWidget(self.tax_checkbox)

        # Submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.setStyleSheet("background-color: lightgreen")
        self.submit_button.setFixedHeight(button_height)  # Match height with other buttons
        data_entry_layout.addWidget(self.submit_button)

        # Set the height of the data entry area
        self.setFixedHeight(40)

        # Add data entry layout to the main layout
        main_layout.addLayout(data_entry_layout)