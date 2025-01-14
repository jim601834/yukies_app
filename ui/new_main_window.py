import sys
import os
import json
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea, QGridLayout, QTableView, QSizePolicy, QStackedWidget
from PySide6.QtCore import Qt
from yukies_app.ui.data_entry_widget import DataEntryWidget  # Use absolute import
from yukies_app.ui.app_control import AppControlWidget  # Import AppControlWidget
from yukies_app.ui.clickable_label import ClickableLabel  # Import ClickableLabel

def load_transition_rules(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

class NewMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Main Window")

        # Load transition rules
        self.transition_rules = load_transition_rules('F:/yukies_project/page_transitions_202501130959.json')["page_transitions"]

        # Track current page
        self.current_page = 1

        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)

        # Create a horizontal layout for the control and data entry widgets
        control_data_layout = QHBoxLayout()
        self.main_layout.addLayout(control_data_layout)

        # Create and add the app control widget
        self.app_control_widget = AppControlWidget()
        control_data_layout.addWidget(self.app_control_widget)

        # Create and add the data entry widget
        self.data_entry_widget = DataEntryWidget()
        control_data_layout.addWidget(self.data_entry_widget)

        # Create a stacked widget for the pages
        self.stacked_widget = QStackedWidget()
        self.main_layout.addWidget(self.stacked_widget)

        # Create pages
        self.create_pages()

        # Maximize the window
        self.showMaximized()

    def create_pages(self):
        self.page_1_widget = self.create_page_1()
        self.page_2_widget = self.create_page_2()
        self.page_3_widget = self.create_page_3()
        self.page_4_widget = self.create_page_4()

        self.stacked_widget.addWidget(self.page_1_widget)
        self.stacked_widget.addWidget(self.page_2_widget)
        self.stacked_widget.addWidget(self.page_3_widget)
        self.stacked_widget.addWidget(self.page_4_widget)

    def create_page_1(self):
        page_widget = QWidget()
        grid_layout = QGridLayout(page_widget)
        headings = ["Budget", "Transaction Detail", "Payment Methods", "Analysis"]
        for i in range(2):
            for j in range(2):
                scroll_area = QScrollArea()
                scroll_area.setWidgetResizable(True)
                area_widget = QWidget()
                area_layout = QVBoxLayout(area_widget)

                # Add heading to each area
                heading_label = ClickableLabel(headings[i * 2 + j])
                heading_label.setAlignment(Qt.AlignCenter)
                heading_label.setStyleSheet("font-size: 8pt; background-color: lightgray")
                heading_label.clicked.connect(self.handle_title_click)
                area_layout.addWidget(heading_label)

                # Add a table view to each area
                table_view = QTableView()
                area_layout.addWidget(table_view)

                scroll_area.setWidget(area_widget)
                scroll_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                grid_layout.addWidget(scroll_area, i, j)

        # Set the grid layout to expand and fill the remaining space
        grid_layout.setRowStretch(0, 1)
        grid_layout.setRowStretch(1, 1)
        grid_layout.setColumnStretch(0, 1)
        grid_layout.setColumnStretch(1, 1)

        return page_widget

    def create_page_2(self):
        page_widget = QWidget()
        grid_layout = QGridLayout(page_widget)
        headings = ["Budget", "Transaction Detail", "Analysis"]
        positions = [(0, 0), (0, 1), (1, 1)]
        
        # Budget area (full height on the left)
        scroll_area_budget = QScrollArea()
        scroll_area_budget.setWidgetResizable(True)
        area_widget_budget = QWidget()
        area_layout_budget = QVBoxLayout(area_widget_budget)

        heading_label_budget = ClickableLabel(headings[0])
        heading_label_budget.setAlignment(Qt.AlignCenter)
        heading_label_budget.setStyleSheet("font-size: 8pt; background-color: lightgray")
        heading_label_budget.clicked.connect(self.handle_title_click)
        area_layout_budget.addWidget(heading_label_budget)

        table_view_budget = QTableView()
        area_layout_budget.addWidget(table_view_budget)

        scroll_area_budget.setWidget(area_widget_budget)
        scroll_area_budget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid_layout.addWidget(scroll_area_budget, 0, 0, 2, 1)  # Span 2 rows

        # Transaction Detail and Analysis (right side)
        for index, (i, j) in enumerate(positions[1:]):
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            area_widget = QWidget()
            area_layout = QVBoxLayout(area_widget)

            heading_label = ClickableLabel(headings[index + 1])
            heading_label.setAlignment(Qt.AlignCenter)
            heading_label.setStyleSheet("font-size: 8pt; background-color: lightgray")
            heading_label.clicked.connect(self.handle_title_click)
            area_layout.addWidget(heading_label)

            table_view = QTableView()
            area_layout.addWidget(table_view)

            scroll_area.setWidget(area_widget)
            scroll_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            grid_layout.addWidget(scroll_area, i, j)

        # Set the grid layout to expand and fill the remaining space
        grid_layout.setRowStretch(0, 1)
        grid_layout.setRowStretch(1, 1)
        grid_layout.setColumnStretch(0, 1)
        grid_layout.setColumnStretch(1, 1)

        return page_widget

    def create_page_3(self):
        page_widget = QWidget()
        grid_layout = QGridLayout(page_widget)
        headings = ["Budget", "Payment Methods", "Transaction Detail"]
        
        # Budget (upper left)
        scroll_area_budget = QScrollArea()
        scroll_area_budget.setWidgetResizable(True)
        area_widget_budget = QWidget()
        area_layout_budget = QVBoxLayout(area_widget_budget)

        heading_label_budget = ClickableLabel(headings[0])
        heading_label_budget.setAlignment(Qt.AlignCenter)
        heading_label_budget.setStyleSheet("font-size: 8pt; background-color: lightgray")
        heading_label_budget.clicked.connect(self.handle_title_click)
        area_layout_budget.addWidget(heading_label_budget)

        table_view_budget = QTableView()
        area_layout_budget.addWidget(table_view_budget)

        scroll_area_budget.setWidget(area_widget_budget)
        scroll_area_budget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid_layout.addWidget(scroll_area_budget, 0, 0)

        # Payment Methods (lower left)
        scroll_area_payment_methods = QScrollArea()
        scroll_area_payment_methods.setWidgetResizable(True)
        area_widget_payment_methods = QWidget()
        area_layout_payment_methods = QVBoxLayout(area_widget_payment_methods)

        heading_label_payment_methods = ClickableLabel(headings[1])
        heading_label_payment_methods.setAlignment(Qt.AlignCenter)
        heading_label_payment_methods.setStyleSheet("font-size: 8pt; background-color: lightgray")
        heading_label_payment_methods.clicked.connect(self.handle_title_click)
        area_layout_payment_methods.addWidget(heading_label_payment_methods)

        table_view_payment_methods = QTableView()
        area_layout_payment_methods.addWidget(table_view_payment_methods)

        scroll_area_payment_methods.setWidget(area_widget_payment_methods)
        scroll_area_payment_methods.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid_layout.addWidget(scroll_area_payment_methods, 1, 0)

        # Transaction Detail (full height on the right)
        scroll_area_transaction = QScrollArea()
        scroll_area_transaction.setWidgetResizable(True)
        area_widget_transaction = QWidget()
        area_layout_transaction = QVBoxLayout(area_widget_transaction)

        heading_label_transaction = ClickableLabel(headings[2])
        heading_label_transaction.setAlignment(Qt.AlignCenter)
        heading_label_transaction.setStyleSheet("font-size: 8pt; background-color: lightgray")
        heading_label_transaction.clicked.connect(self.handle_title_click)
        area_layout_transaction.addWidget(heading_label_transaction)

        table_view_transaction = QTableView()
        area_layout_transaction.addWidget(table_view_transaction)

        scroll_area_transaction.setWidget(area_widget_transaction)
        scroll_area_transaction.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid_layout.addWidget(scroll_area_transaction, 0, 1, 2, 1)  # Span 2 rows

        # Set the grid layout to expand and fill the remaining space
        grid_layout.setRowStretch(0, 1)
        grid_layout.setRowStretch(1, 1)
        grid_layout.setColumnStretch(0, 1)
        grid_layout.setColumnStretch(1, 1)

        return page_widget

    def create_page_4(self):
        page_widget = QWidget()
        grid_layout = QGridLayout(page_widget)
        headings = ["Budget", "Transaction Detail"]
        positions = [(0, 0), (0, 1)]
        for index, (i, j) in enumerate(positions):
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            area_widget = QWidget()
            area_layout = QVBoxLayout(area_widget)

            # Add heading to each area
            heading_label = ClickableLabel(headings[index])
            heading_label.setAlignment(Qt.AlignCenter)
            heading_label.setStyleSheet("font-size: 8pt; background-color: lightgray")
            heading_label.clicked.connect(self.handle_title_click)
            area_layout.addWidget(heading_label)

            # Add a table view to each area
            table_view = QTableView()
            area_layout.addWidget(table_view)

            scroll_area.setWidget(area_widget)
            scroll_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            grid_layout.addWidget(scroll_area, i, j)

        # Set the grid layout to expand and fill the remaining space
        grid_layout.setRowStretch(0, 1)
        grid_layout.setColumnStretch(0, 1)
        grid_layout.setColumnStretch(1, 1)

        return page_widget

    def handle_title_click(self):
        sender = self.sender()
        if sender is None:
            print("Error: sender is None")
            return

        title = sender.text()
        action = ""
        if title == "Budget":
            action = "1"
        elif title == "Transaction Detail":
            action = "2"
        elif title == "Payment Methods":
            action = "3"
        elif title == "Analysis":
            action = "4"
        else:
            return

        for rule in self.transition_rules:
            if rule["from_page"] == str(self.current_page) and rule["clicked_area"] == action:
                next_page = int(rule["to_page"])  # Convert to integer
                self.stacked_widget.setCurrentIndex(next_page - 1)
                self.current_page = next_page
                break