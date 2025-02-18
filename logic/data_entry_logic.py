class DataEntryLogic:
    def __init__(self, db_handler):
        self.db_handler = db_handler

    def fetch_data_from_view(self, view_name):
        query = f"SELECT name FROM {view_name}"
        return self.db_handler.execute_query(query)['name'].tolist()

    def fetch_pay_to_view(self, name):
        query = "SELECT category, pmt_method FROM pay_to_view WHERE name = :name"
        params = {'name': name}
        result = self.db_handler.execute_query(query, params)
        if not result.empty:
            return result.iloc[0]['category'], result.iloc[0]['pmt_method']
        return None, None

    def fetch_default_account_from_budget(self, category):
        query = "SELECT account_name FROM budget WHERE category = :category"
        params = {'category': category}
        result = self.db_handler.execute_query(query, params)
        if not result.empty:
            return result.iloc[0]['account_name']
        return None

    def load_combo_box_data(self, t_code):
        to_view = f"{t_code}_to_view"
        from_view = f"{t_code}_from_view"

        to_accounts = self.fetch_data_from_view(to_view)
        from_accounts = self.fetch_data_from_view(from_view)

        return to_accounts, from_accounts

    def handle_pay_button_logic(self, combo_box_to_text):
        category, pmt_method = self.fetch_pay_to_view(combo_box_to_text)

        tax_checked = False
        default_account = None

        if category:
            if category == "Medical":
                tax_checked = True
            if pmt_method:
                default_account = pmt_method
            else:
                default_account = self.fetch_default_account_from_budget(category)

        return tax_checked, default_account