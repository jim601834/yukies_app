from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class PaymentMethodsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        
        # Add a label with the title
        title_label = QLabel("Payment Methods Area")
        title_label.setStyleSheet("font-weight: bold; font-size: 14pt;")
        layout.addWidget(title_label)
        
        # Add example content
        for i in range(10):
            layout.addWidget(QLabel(f"Payment Methods Area - Item {i+1}"))