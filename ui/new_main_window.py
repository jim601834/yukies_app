import sys
import os

# Add the parent directory to sys.path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea, QGridLayout, QLabel, QTableView, QSizePolicy
from PySide6.QtCore import Qt
from yukies_app.ui.data_entry_widget import DataEntryWidget  # Use absolute import
from yukies_app.ui.app_control import AppControlWidget  # Import AppControlWidget

class NewMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Main Window")

        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Create a horizontal layout for the control and data entry widgets
        control_data_layout = QHBoxLayout()
        main_layout.addLayout(control_data_layout)

        # Create and add the app control widget
        self.app_control_widget = AppControlWidget()
        control_data_layout.addWidget(self.app_control_widget)

        # Create and add the data entry widget
        self.data_entry_widget = DataEntryWidget()
        control_data_layout.addWidget(self.data_entry_widget)

        # Create a grid layout for the scrollable areas
        self.grid_layout = QGridLayout()
        main_layout.addLayout(self.grid_layout)

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
                scroll_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.grid_layout.addWidget(scroll_area, i, j)

        # Set the grid layout to expand and fill the remaining space
        self.grid_layout.setRowStretch(0, 1)
        self.grid_layout.setRowStretch(1, 1)
        self.grid_layout.setColumnStretch(0, 1)
        self.grid_layout.setColumnStretch(1, 1)

        # Maximize the window
        self.showMaximized()