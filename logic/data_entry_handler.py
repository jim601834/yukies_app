from database.db_handler import DBHandler

class DataEntryHandler:
    def __init__(self, db_handler: DBHandler):
        self.db_handler = db_handler

    def load_pay_combo_boxes(self):
        try:
            # Load the "To" combo box from new_schema.pay_to_view
            query = "SELECT acct_name FROM new_schema.pay_to_view"
            pay_to_accounts = self.db_handler.fetch_all(query)

            # Load the "From" combo box from new_schema.pay_from_view
            query = "SELECT acct_name FROM new_schema.pay_from_view"
            pay_from_accounts = self.db_handler.fetch_all(query)

            return pay_to_accounts, pay_from_accounts

        except Exception as e:
            raise Exception(f"An error occurred while loading combo boxes: {e}")

    def load_transfer_combo_boxes(self):
        try:
            # Load the "To" combo box from new_schema.transfer_to_view
            query = "SELECT acct_name FROM new_schema.transfer_to_view"
            transfer_to_accounts = self.db_handler.fetch_all(query)

            # Load the "From" combo box from new_schema.transfer_from_view
            query = "SELECT acct_name FROM new_schema.transfer_from_view"
            transfer_from_accounts = self.db_handler.fetch_all(query)

            return transfer_to_accounts, transfer_from_accounts

        except Exception as e:
            raise Exception(f"An error occurred while loading combo boxes: {e}")

    def load_deposit_combo_boxes(self):
        try:
            # Load the "To" combo box from new_schema.deposit_to_view
            query = "SELECT acct_name FROM new_schema.deposit_to_view"
            deposit_to_accounts = self.db_handler.fetch_all(query)

            # Load the "From" combo box from new_schema.deposit_from_view
            query = "SELECT acct_name FROM new_schema.deposit_from_view"
            deposit_from_accounts = self.db_handler.fetch_all(query)

            return deposit_to_accounts, deposit_from_accounts

        except Exception as e:
            raise Exception(f"An error occurred while loading combo boxes: {e}")

    def load_withdraw_combo_boxes(self):
        try:
            # Load the "From" combo box from new_schema.withdraw_from_view
            query = "SELECT acct_name FROM new_schema.withdraw_from_view"
            withdraw_from_accounts = self.db_handler.fetch_all(query)

            return withdraw_from_accounts

        except Exception as e:
            raise Exception(f"An error occurred while loading combo boxes: {e}")

    def fill_qlog_entry(self, to_account, data_entry_widget, t_code_holder):
        # Implement the logic to fill the qlog entry based on the to_account and other parameters
        data_entry_widget.qlog_entry['to_account'] = to_account
        data_entry_widget.qlog_entry['t_code'] = t_code_holder
        # Add any additional logic needed to fill the qlog entry

    def construct_qlog_entry(self, data_entry_widget, t_code_holder):
        # Implement the logic to construct the qlog entry based on the data entry widget and t_code_holder
        qlog_entry = {
            'to_account': data_entry_widget.qlog_entry.get('to_account'),
            't_code': t_code_holder,
            'from_account': data_entry_widget.combo_box_from.currentText(),
            'amount': data_entry_widget.amount_input.value(),
            'date': QDateTime.currentDateTime().toString(Qt.ISODate)
        }
        return qlog_entry