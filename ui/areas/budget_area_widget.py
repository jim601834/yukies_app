import sys
import os

# Add the parent directory to sys.path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableView

class BudgetAreaWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        
        # Add a label with the title
        title_label = QLabel("Budget")
        title_label.setStyleSheet("font-weight: bold; font-size: 14pt;")
        layout.addWidget(title_label)

        
        
        # Set the background color to light gray
        self.setStyleSheet("background-color: lightgray;")
        
        # Add a table view to create a large content area
        table_view = QTableView()
        layout.addWidget(table_view)