class ComboBoxLogic:
    def __init__(self, main_window, db_handler):
        self.main_window = main_window
        self.db_handler = db_handler
        self.populate_combo_boxes()

    def populate_combo_boxes(self):
        # Example logic to populate combo boxes
        accounts = self.get_accounts()
        self.main_window.data_entry_widget.combo_box_to.addItems(accounts)
        self.main_window.data_entry_widget.combo_box_from.addItems(accounts)

    def get_accounts(self):
        query = "SELECT acct_name FROM new_schema.accounts"
        results = self.db_handler.fetch_all(query)
        return [result[0] for result in results]