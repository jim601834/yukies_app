from PySide6.QtWidgets import QWidget, QVBoxLayout, QComboBox, QPushButton, QDoubleSpinBox

class DataEntryWidget(QWidget):
    def __init__(self):
        super(DataEntryWidget, self).__init__()

        # Initialize qlog_entry attribute
        self.qlog_entry = {}

        # Set up the layout and widgets
        layout = QVBoxLayout(self)

        self.combo_box_to = QComboBox()
        self.combo_box_to.setEditable(True)  # Make the combo box editable
        self.combo_box_from = QComboBox()
        self.combo_box_from.setEditable(True)  # Make the combo box editable
        self.amount_input = QDoubleSpinBox()
        self.amount_input.setMaximum(1000000)
        self.submit_button = QPushButton("Submit")
        self.maintain_button = QPushButton("Maintain")
        self.withdraw_button = QPushButton("Withdraw")
        self.deposit_button = QPushButton("Deposit")
        self.transfer_button = QPushButton("Transfer")
        self.pay_button = QPushButton("Pay")

        layout.addWidget(self.combo_box_to)
        layout.addWidget(self.combo_box_from)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.maintain_button)
        layout.addWidget(self.withdraw_button)
        layout.addWidget(self.deposit_button)
        layout.addWidget(self.transfer_button)
        layout.addWidget(self.pay_button)

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