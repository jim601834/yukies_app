from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy

class AppControlWidget(QWidget):
    def __init__(self, parent=None):
        super(AppControlWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        # Add a vertical spacer to lower the buttons
        spacer = QSpacerItem(22, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        layout.addSpacerItem(spacer)

        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.setSpacing(5)

        # "Reset" button
        self.reset_button = QPushButton("Reset")
        self.reset_button.setStyleSheet("background-color: lightgreen; border: 3px solid red; font-size: 10pt; margin: 0px;")
        self.reset_button.setFixedHeight(32)
        self.reset_button.setFixedWidth(67)
        button_layout.addWidget(self.reset_button)

        # "Maintain" button
        self.maintain_button = QPushButton("Maintain")
        self.maintain_button.setStyleSheet("background-color: lightgray; font-size: 10pt;")
        self.maintain_button.setFixedHeight(29)
        self.maintain_button.setFixedWidth(67)
        button_layout.addWidget(self.maintain_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)