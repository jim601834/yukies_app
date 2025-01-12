from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class AnalysisAreaWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        QA!QA!QA!QA!QA!QA!QA!QA!QA!QA!QA!QA!QA!                                                                   
        # Add a label with the title
        title_label = QLabel("Analysis Area")
        title_label.setStyleSheet("font-weight: bold; font-size: 14pt;")
        layout.addWidget(title_label)
        
        # Add example content
        for i in range(10):
            layout.addWidget(QLabel(f"Analysis Area - Item {i+1}"))