from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt

class DateRangeButtonsArea(QWidget):
    def __init__(self, transaction_detail_area):
        super(DateRangeButtonsArea, self).__init__()
        self.transaction_detail_area = transaction_detail_area
        self.layout = QVBoxLayout(self)

        self.heading_label = QLabel("Date Range")
        self.heading_label.setAlignment(Qt.AlignCenter)
        self.heading_label.setStyleSheet("font-size: 8pt; background-color: lightgray")
        self.layout.addWidget(self.heading_label)

        self.current_month_button = QPushButton("Current Month")
        self.current_month_button.clicked.connect(self.show_current_month)
        self.layout.addWidget(self.current_month_button)

        self.last_month_button = QPushButton("Last Month")
        self.last_month_button.clicked.connect(self.show_last_month)
        self.layout.addWidget(self.last_month_button)

        self.last_three_months_button = QPushButton("Last 3 Months")
        self.last_three_months_button.clicked.connect(self.show_last_three_months)
        self.layout.addWidget(self.last_three_months_button)

        self.last_six_months_button = QPushButton("Last 6 Months")
        self.last_six_months_button.clicked.connect(self.show_last_six_months)
        self.layout.addWidget(self.last_six_months_button)

        self.last_year_button = QPushButton("Last Year")
        self.last_year_button.clicked.connect(self.show_last_year)
        self.layout.addWidget(self.last_year_button)

    def show_current_month(self):
        self.transaction_detail_area.load_data()

    def show_last_month(self):
        # Implement logic to load data for the last month
        pass

    def show_last_three_months(self):
        # Implement logic to load data for the last 3 months
        pass

    def show_last_six_months(self):
        # Implement logic to load data for the last 6 months
        pass

    def show_last_year(self):
        # Implement logic to load data for the last year
        pass