from PySide6.QtCore import QObject, Signal

class DataEntryLogic(QObject):
    tax_checkbox_update = Signal(bool)  # Signal to update the tax checkbox
    restart_app_signal = Signal()  # Signal to restart the app

    def __init__(self, db_handler, data_entry_widget):
        super().__init__()
        self.db_handler = db_handler
        self.data_entry_widget = data_entry_widget

        # Connect signals
        self.data_entry_widget.function_button_clicked.connect(self.process_function_button)
        self.data_entry_widget.cb1_account_selected.connect(self.cb1_account_selected)
        self.data_entry_widget.submit_button_clicked.connect(self.submit_button_logic)

    def fetch_data_from_view(self, view_name):
        query = f"SELECT name FROM new_schema.{view_name}"
        try:
            result = self.db_handler.execute_query(query)
            return result['name'].tolist()
        except Exception as e:
            print(f"fetch_data_from_view: Database error: {e}")
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

        print(f"load_combo_box_data: Loaded combo box data for t_code: {t_code}")
        self.data_entry_widget.update_combo_boxes(to_accounts, from_accounts, cb1_placeholder, cb2_placeholder)

    def process_function_button(self, t_code):
        print(f"process_function_button: Received signal to process function button: {t_code}")
        self.load_combo_box_data(t_code)

    def cb1_account_selected(self, data):
        t_code = data['t_code']
        account_name = data['account_name']
        if t_code not in ["pay", "refund"]:
            return

        query = "SELECT category, pmt_method FROM new_schema.top_level_view WHERE name = :name"
        params = {'name': account_name}
        try:
            result = self.db_handler.execute_query(query, params)
            print(f"cb1_account_selected: Fetched data for account_name: {account_name}")
            if not result.empty:
                category = result.iloc[0]['category']
                pmt_method = result.iloc[0]['pmt_method']
                if pmt_method:
                    self.data_entry_widget.set_cb2_default(pmt_method)  # Set cb2 default value without changing the dropdown list
                else:
                    budget_query = "SELECT pmt_method FROM new_schema.budget WHERE category = :category"
                    budget_params = {'category': category}
                    budget_result = self.db_handler.execute_query(budget_query, budget_params)
                    if not budget_result.empty:
                        budget_pmt_method = budget_result.iloc[0]['pmt_method']
                        self.data_entry_widget.set_cb2_default(budget_pmt_method)  # Set cb2 default value without changing the dropdown list

                if category == "Medical":
                    self.tax_checkbox_update.emit(True)
                else:
                    self.tax_checkbox_update.emit(False)
        except Exception as e:
            print(f"cb1_account_selected: Database error: {e}")

    def submit_button_logic(self, data):
        print(f"submit_button_logic: Submit button clicked with data: {data}")
        # Process the submission logic here
        try:
            # Example: Insert data into the database
            insert_query = """
            INSERT INTO new_schema.transactions (t_code, date, cb1, cb2, amount, comment, tax)
            VALUES (:t_code, :date, :cb1, :cb2, :amount, :comment, :tax)
            """
            self.db_handler.execute_query(insert_query, data)
            print("submit_button_logic: Data inserted successfully")

            # Emit signal to restart the app
            self.restart_app_signal.emit()
        except Exception as e:
            print(f"submit_button_logic: Error during submission: {e}")

    def restart_app(self):
        print("restart_app: Restarting the app...")
        # Logic to reset and reload the UI components
        # For example, you can emit signals to reload different parts of the UI
        self.load_combo_box_data("pay")
        self.load_combo_box_data("refund")
        self.load_combo_box_data("deposit")
        self.load_combo_box_data("withdraw")
        self.load_combo_box_data("transfer")