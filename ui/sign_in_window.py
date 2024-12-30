from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QApplication

class SignInWindow(QDialog):
    def __init__(self):
        super(SignInWindow, self).__init__()
        self.setWindowTitle("Sign In")
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.label = QLabel("Click 'Sign In' to continue")
        layout.addWidget(self.label)

        self.sign_in_button = QPushButton("Sign In")
        layout.addWidget(self.sign_in_button)

        self.setLayout(layout)

        # Connect the sign-in button to the sign-in method
        self.sign_in_button.clicked.connect(self.sign_in)

    def sign_in(self):
        # For now, just accept the dialog to simulate a successful sign-in
        self.accept()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = SignInWindow()
    window.exec()