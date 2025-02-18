import sys
import os

# Add the parent directory to sys.path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QScrollArea, QGridLayout, QLabel, QTableView
from PySide6.QtCore import Qt
from yukies_app.ui.data_entry_widget import DataEntryWidget  # Use absolute import
from yukies_app.database.db_handler import DBHandler  # Import DBHandler

class NewMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Main Window")

        # Initialize DBHandler with the actual PostgreSQL database URL
        self.db_handler = DBHandler("postgresql://postgres:sasuke@localhost:5433/yukies_db")

        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create and add the data entry widget with db_handler
        self.data_entry_widget = DataEntryWidget(self.db_handler)
        layout.addWidget(self.data_entry_widget)

        # Create a grid layout for the scrollable areas
        self.grid_layout = QGridLayout()
        layout.addLayout(self.grid_layout)

        headings = ["Budget", "Transaction Detail", "Area 3", "Area 4"]
        for i in range(2):
            for j in range(2):
                scroll_area = QScrollArea()
                scroll_area.setWidgetResizable(True)
                area_widget = QWidget()
                area_layout = QVBoxLayout(area_widget)

                # Add heading to each area
                heading_label = QLabel(headings[i * 2 + j])
                heading_label.setAlignment(Qt.AlignCenter)
                heading_label.setStyleSheet("font-size: 8pt; background-color: lightgray")
                area_layout.addWidget(heading_label)

                # Add a table view to each area
                table_view = QTableView()
                area_layout.addWidget(table_view)

                scroll_area.setWidget(area_widget)
                self.grid_layout.addWidget(scroll_area, i, j)

        # Maximize the window
        self.showMaximized()