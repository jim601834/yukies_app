from database.db_handler import DBHandler

class TransactionHandler:
    def __init__(self, db_handler: DBHandler):
        self.db_handler = db_handler

    def handle_transaction(self, qlog_entry, from_account, to_account, amount):
        try:
            print("Starting transaction...")  # Debugging
            print("Qlog Entry:", qlog_entry)  # Debugging

            # Begin transaction
            self.db_handler.begin_transaction()

            # Insert the qlog entry into the database
            query = """
                INSERT INTO new_schema.qlog (entry_date, entry_time, service_date, amount, from_account, "comment", deduction, t_code, distance, to_account, category)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id
            """
            qlog_id = self.db_handler.fetch_one(query, (
                qlog_entry['entry_date'], qlog_entry['entry_time'], qlog_entry['service_date'], qlog_entry['amount'],
                qlog_entry['from_account'], qlog_entry['comment'], qlog_entry['deduction'], qlog_entry['t_code'],
                qlog_entry['distance'], qlog_entry['to_account'], qlog_entry['category']
            ))[0]
            print("Inserted qlog entry with ID:", qlog_id)  # Debugging

            # Insert the actions entries into the database
            actions = [
                (qlog_id, to_account, float(amount)),
                (qlog_id, from_account, -float(amount))
            ]
            query = """
                INSERT INTO new_schema.actions (qlog_id, account_name, amount)
                VALUES (%s, %s, %s)
            """
            for action in actions:
                self.db_handler.execute_query(query, action)
                print("Inserted action:", action)  # Debugging

            # Commit transaction
            self.db_handler.commit_transaction()
            print("Transaction committed successfully.")  # Debugging

        except Exception as e:
            # Rollback transaction in case of error
            self.db_handler.rollback_transaction()
            print("Transaction rolled back due to error:", e)  # Debugging
            raise e