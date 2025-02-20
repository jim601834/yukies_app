from PySide6.QtCore import QObject, Signal

class DataEntryLogic(QObject):
    combo_box_data_loaded = Signal(list, list, str, str)  # Signal to emit combo box data with placeholders
    tax_checkbox_update = Signal(bool)  # Signal to update the tax checkbox

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

    def cb1_account_selected(self, data):
        t_code = data['t_code']
        account_name = data['account_name']
        if t_code != "pay":
            return

        query = "SELECT category, pmt_method FROM new_schema.top_level_view WHERE name = :name"
        params = {'name': account_name}
        try:
            result = self.db_handler.execute_query(query, params)
            if not result.empty:
                category = result.iloc[0]['category']
                pmt_method = result.iloc[0]['pmt_method']
                if pmt_method:
                    self.combo_box_data_loaded.emit([], [pmt_method], "", "")  # Set cb2 default value
                else:
                    budget_query = "SELECT pmt_method FROM new_schema.budget WHERE category = :category"
                    budget_params = {'category': category}
                    budget_result = self.db_handler.execute_query(budget_query, budget_params)
                    if not budget_result.empty:
                        budget_pmt_method = budget_result.iloc[0]['pmt_method']
                        self.combo_box_data_loaded.emit([], [budget_pmt_method], "", "")  # Set cb2 default value

                if category == "Medical":
                    self.tax_checkbox_update.emit(True)
                else:
                    self.tax_checkbox_update.emit(False)
        except Exception as e:
            print(f"Database error: {e}")

    def submit_button_logic(self, data):
        print(f"Submit button clicked with data: {data}")