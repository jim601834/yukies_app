from database.db_handler import DBHandler
from ui.areas.budget_area import BudgetArea
from ui.areas.transaction_detail_area import TransactionDetailArea
from ui.areas.payment_methods_area import PaymentMethodsArea
from ui.areas.date_range_buttons_area import DateRangeButtonsArea
from logic.combo_box_logic import ComboBoxLogic
from PySide6.QtWidgets import QWidget  # Add this import

class AppInitializer:
    def __init__(self, main_window, db_config):
        self.main_window = main_window
        self.db_handler = DBHandler(db_config)

    def initialize(self):
        # Initialize ComboBoxLogic
        self.main_window.combo_box_logic = ComboBoxLogic(self.main_window, self.db_handler)

        # Initialize areas
        self.main_window.budget_area = BudgetArea(self.db_handler)
        self.main_window.transaction_detail_area = TransactionDetailArea(self.db_handler)
        self.main_window.payment_methods_area = PaymentMethodsArea(self.db_handler)
        self.main_window.date_range_buttons_area = DateRangeButtonsArea(self.main_window.transaction_detail_area)

        # Add scrollable areas to the grid layout
        self.main_window.add_scroll_area(self.main_window.budget_area, 0, 0)
        self.main_window.add_scroll_area(self.main_window.transaction_detail_area, 0, 1)
        self.main_window.add_scroll_area(self.main_window.payment_methods_area, 1, 0)
        self.main_window.add_scroll_area(QWidget(), 1, 1)  # Blank area for now

        # Let each area handle its own data loading
        self.main_window.budget_area.load_data()
        self.main_window.transaction_detail_area.load_data(self.main_window.current_category)
        self.main_window.payment_methods_area.load_data()