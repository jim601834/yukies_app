import sys
import json
from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QHBoxLayout, QWidget,
                              QStackedWidget, QApplication)
from PySide6.QtCore import Signal, Slot
from .data_entry_widget import DataEntryWidget
from .app_control import AppControlWidget
from .page_definitions import PageCreator
from ..logic.budget_logic import BudgetLogic
from ..logic.payment_methods_logic import PaymentMethodsLogic
from ..logic.transaction_detail_logic import TransactionDetailLogic
from ..database.db_handler import DBHandler

def load_transition_rules(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

class NewMainWindow(QMainWindow):
    area_expanded = Signal(bool)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Main Window")

        # Initialize database and logic components
        db_url = 'postgresql://postgres:sasuke@localhost:5433/yukies_db'
        self.db_handler = DBHandler(db_url)
        
        # Initialize logic components
        self.transaction_detail_logic = TransactionDetailLogic(self.db_handler)
        self.budget_logic = BudgetLogic(self.db_handler, self.transaction_detail_logic)
        self.payment_methods_logic = PaymentMethodsLogic(self.db_handler, self.transaction_detail_logic)

        # Initialize page creator
        self.page_creator = PageCreator(self)

        # Load transition rules
        self.transition_rules = load_transition_rules('F:/yukies_project/yukies_app/page_transitions.json')["page_transitions"]
        self.current_page = 1

        # Create UI components
        self.setup_ui()
        
        # Register views and load data
        self.register_transaction_views()
        self.restart_logic(expanded=False)
        
        self.showMaximized()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)

        # Control and data entry widgets
        control_data_layout = QHBoxLayout()
        self.main_layout.addLayout(control_data_layout)

        self.app_control_widget = AppControlWidget()
        control_data_layout.addWidget(self.app_control_widget)
        
        self.data_entry_widget = DataEntryWidget()
        control_data_layout.addWidget(self.data_entry_widget)

        # Stacked widget for pages
        self.stacked_widget = QStackedWidget()
        self.main_layout.addWidget(self.stacked_widget)

        # Create pages
        self.create_pages()

        # Connect signals
        self.area_expanded.connect(self.handle_area_expansion)

    def create_pages(self):
        self.page_1_widget = self.page_creator.create_page_1()
        self.page_2_widget = self.page_creator.create_page_2()
        self.page_3_widget = self.page_creator.create_page_3()
        self.page_4_widget = self.page_creator.create_page_4()

        self.stacked_widget.addWidget(self.page_1_widget)
        self.stacked_widget.addWidget(self.page_2_widget)
        self.stacked_widget.addWidget(self.page_3_widget)
        self.stacked_widget.addWidget(self.page_4_widget)

    def register_transaction_views(self):
        try:
            views = [
                self.table_view_transaction_detail_page_1,
                self.table_view_transaction_detail_page_2,
                self.table_view_transaction_detail_page_3,
                self.table_view_transaction_detail_page_4
            ]
            for view in views:
                if view is not None:
                    self.transaction_detail_logic.register_table_view(view)
            print(f"Successfully registered {len(views)} transaction views")
        except Exception as e:
            print(f"Error registering transaction views: {e}")

    def handle_title_click(self):
        sender = self.sender()
        if sender is None:
            return

        title = sender.text()
        action = {"Budget": "1", "Transaction Detail": "2", 
                 "Payment Methods": "3", "Analysis": "4"}.get(title, "")

        if action:
            for rule in self.transition_rules:
                if (rule["from_page"] == str(self.current_page) and 
                    rule["clicked_area"] == action):
                    next_page = int(rule["to_page"])
                    self.stacked_widget.setCurrentIndex(next_page - 1)
                    self.current_page = next_page
                    break

    @Slot(bool)
    def handle_area_expansion(self, expanded):
        print(f"Area expanded: {expanded}")
        self.restart_logic(expanded)

    def restart_logic(self, expanded):
        try:
            # Load and display budget data
            df = self.budget_logic.load_budget_data(expanded)
            
            budget_views = [
                self.table_view_budget_page_1,
                self.table_view_budget_page_2,
                self.table_view_budget_page_3,
                self.table_view_budget_page_4
            ]
            for view in budget_views:
                self.budget_logic.display_budget_data(df, view)

            # Load and display payment methods
            df_payment_methods = self.payment_methods_logic.load_payment_methods_data()
            self.payment_methods_logic.display_payment_methods_data(
                df_payment_methods, self.table_view_payment_methods_page_1)
            self.payment_methods_logic.display_payment_methods_data(
                df_payment_methods, self.table_view_payment_methods_page_3)
            
            # Load and display transaction details
            df_transaction = self.transaction_detail_logic.load_transaction_detail_data()
            for view in self.transaction_detail_logic._current_table_views:
                self.transaction_detail_logic.display_transaction_detail_data(
                    df_transaction, view)

        except Exception as e:
            print(f"Error in restart_logic: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewMainWindow()
    window.show()
    sys.exit(app.exec())