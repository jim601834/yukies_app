import sys
import os
from PySide6.QtWidgets import QApplication

# Add the parent directory to sys.path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

# Debugging statement to print sys.path
# print("sys.path:", sys.path)

from yukies_app.ui.new_main_window import NewMainWindow  # Use absolute import

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewMainWindow()
    window.showMaximized()  # Ensure the main window is shown maximized
    sys.exit(app.exec())