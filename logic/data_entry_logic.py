from PySide6.QtCore import QObject, Signal

class DataEntryLogic(QObject):
    combo_box_data_loaded = Signal(list, list, str, str)  # Signal to emit combo box data with placeholders

    def __init__(self, db_handler):
        super().__init__()
        self.db_handler = db_handler

    def fetch_data_from_view(self, view_name):
        query = f"SELECT name FROM new_schema.{view_name}"
        try:
            result = self.db_handler.execute_query(query)
            return result['name'].tolist()
        except Exception as e:
            print(f"Database error: {e}")
            return []

    def load_combo_box_data(self, t_code):
        if t_code == "refund":
            to_view = "refund_to_view"
            from_view = "refund_from_view"
            cb1_placeholder = "Select 'From' Account"
            cb2_placeholder = "Select 'To' Account"
        else:
            to_view = f"{t_code}_to_view"
            from_view = f"{t_code}_from_view"
            cb1_placeholder = "Select 'To' Account"
            cb2_placeholder = "Select 'From' Account"

        to_accounts = self.fetch_data_from_view(to_view)
        from_accounts = self.fetch_data_from_view(from_view)

        print(f"Loaded combo box data for t_code: {t_code}")
        self.combo_box_data_loaded.emit(to_accounts, from_accounts, cb1_placeholder, cb2_placeholder)  # Emit the data

    def process_function_button(self, t_code):
        print(f"Received signal to process function button: {t_code}")
        self.load_combo_box_data(t_code)