from PySide6.QtWidgets import QApplication, QDialog
from ui.sign_in_window import SignInWindow
from ui.new_main_window import NewMainWindow

def main():
    app = QApplication([])

    # Show the sign-in window
    sign_in_window = SignInWindow()
    if sign_in_window.exec() == QDialog.Accepted:
        # Show the main application window upon successful sign-in
        main_window = NewMainWindow()
        main_window.show()
        app.exec()

if __name__ == "__main__":
    main()