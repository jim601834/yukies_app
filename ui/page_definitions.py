from PySide6.QtWidgets import (QWidget, QVBoxLayout, QScrollArea, 
                              QGridLayout, QTableView, QSizePolicy)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from .clickable_label import ClickableLabel

class PageCreator:
    def __init__(self, parent):
        self.parent = parent

    def _create_scroll_area(self, heading):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        area_widget = QWidget()
        area_layout = QVBoxLayout(area_widget)
        area_layout.setContentsMargins(0, 0, 0, 0)
        area_layout.setSpacing(0)

        heading_label = ClickableLabel(heading)
        heading_label.setAlignment(Qt.AlignCenter)
        heading_label.setStyleSheet("font-size: 10pt; background-color: lightgray")
        heading_label.clicked.connect(self.parent.handle_title_click)
        area_layout.addWidget(heading_label)

        table_view = QTableView()
        table_view.setFont(QFont("Arial", 10))
        area_layout.addWidget(table_view)

        scroll_area.setWidget(area_widget)
        scroll_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        return scroll_area, table_view

    def _set_grid_stretches(self, grid_layout, rows=2, cols=2):
        for i in range(rows):
            grid_layout.setRowStretch(i, 1)
        for j in range(cols):
            grid_layout.setColumnStretch(j, 1)

    def create_page_1(self):
        page_widget = QWidget()
        grid_layout = QGridLayout(page_widget)
        grid_layout.setSpacing(0)
        headings = ["Budget", "Transaction Detail", "Payment Methods", "Analysis"]
        
        for i in range(2):
            for j in range(2):
                scroll_area, table_view = self._create_scroll_area(headings[i * 2 + j])
                grid_layout.addWidget(scroll_area, i, j)
                
                heading = headings[i * 2 + j]
                if heading == "Budget":
                    self.parent.table_view_budget_page_1 = table_view
                elif heading == "Payment Methods":
                    self.parent.table_view_payment_methods_page_1 = table_view
                elif heading == "Transaction Detail":
                    self.parent.table_view_transaction_detail_page_1 = table_view

        self._set_grid_stretches(grid_layout)
        return page_widget

    def create_page_2(self):
        page_widget = QWidget()
        grid_layout = QGridLayout(page_widget)
        grid_layout.setSpacing(0)
        headings = ["Budget", "Transaction Detail", "Analysis"]

        # Budget (full height left)
        scroll_area, table_view = self._create_scroll_area(headings[0])
        grid_layout.addWidget(scroll_area, 0, 0, 2, 1)
        self.parent.table_view_budget_page_2 = table_view

        # Right side panels
        for i, heading in enumerate(headings[1:]):
            scroll_area, table_view = self._create_scroll_area(heading)
            grid_layout.addWidget(scroll_area, i, 1)
            if heading == "Transaction Detail":
                self.parent.table_view_transaction_detail_page_2 = table_view

        self._set_grid_stretches(grid_layout)
        return page_widget

    def create_page_3(self):
        page_widget = QWidget()
        grid_layout = QGridLayout(page_widget)
        grid_layout.setSpacing(0)
        headings = ["Budget", "Payment Methods", "Transaction Detail"]

        # Left column
        for i, heading in enumerate(headings[:2]):
            scroll_area, table_view = self._create_scroll_area(heading)
            grid_layout.addWidget(scroll_area, i, 0)
            if heading == "Budget":
                self.parent.table_view_budget_page_3 = table_view
            else:
                self.parent.table_view_payment_methods_page_3 = table_view

        # Transaction Detail (full height right)
        scroll_area, table_view = self._create_scroll_area(headings[2])
        grid_layout.addWidget(scroll_area, 0, 1, 2, 1)
        self.parent.table_view_transaction_detail_page_3 = table_view

        self._set_grid_stretches(grid_layout)
        return page_widget

    def create_page_4(self):
        page_widget = QWidget()
        grid_layout = QGridLayout(page_widget)
        grid_layout.setSpacing(0)
        headings = ["Budget", "Transaction Detail"]

        for i, heading in enumerate(headings):
            scroll_area, table_view = self._create_scroll_area(heading)
            grid_layout.addWidget(scroll_area, 0, i)
            if heading == "Budget":
                self.parent.table_view_budget_page_4 = table_view
            else:
                self.parent.table_view_transaction_detail_page_4 = table_view

        self._set_grid_stretches(grid_layout, rows=1, cols=2)
        return page_widget