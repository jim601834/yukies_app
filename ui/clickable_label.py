from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Signal

class ClickableLabel(QLabel):
    clicked = Signal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)