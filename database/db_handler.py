import psycopg2
from datetime import datetime, timedelta
import json
import os

class DBHandler:
    def __init__(self, config_path=None):
        if config_path is None:
            config_path = os.path.join(os.path.dirname(__file__), '../config/config.json')
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        self.conn = None

    def connect(self):
        if self.conn is None or self.conn.closed:
            self.conn = psycopg2.connect(**self.config)

    def close(self):
        if self.conn and not self.conn.closed:
            self.conn.close()

    def get_view_data(self, schema_name, view_name, column_name):
        self.connect()
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(f"SELECT {column_name} FROM {schema_name}.{view_name}")
                rows = cursor.fetchall()
                return [row[0] for row in rows]
        except psycopg2.Error as e:
            print(f"Error fetching data from view {schema_name}.{view_name}: {e}")
            return []
        finally:
            self.close()

    def get_table_data(self, schema_name, table_name, column_name):
        self.connect()
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(f"SELECT {column_name} FROM {schema_name}.{table_name}")
                rows = cursor.fetchall()
                return [row[0] for row in rows]
        except psycopg2.Error as e:
            print(f"Error fetching data from table {schema_name}.{table_name}: {e}")
            return []
        finally:
            self.close()

    def list_views(self):
        self.connect()
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT table_schema, table_name FROM information_schema.views WHERE table_schema NOT IN ('information_schema', 'pg_catalog')")
                views = cursor.fetchall()
                for view in views:
                    print(f"View: {view[0]}.{view[1]}")
        except psycopg2.Error as e:
            print(f"Error listing views: {e}")
        finally:
            self.close()

    def get_nth_weekday_of_month(self, year, month, weekday, n):
        """
        Get the date of the nth specified weekday of the given month and year.
        :param year: int
        :param month: int
        :param weekday: int (0=Monday, 1=Tuesday, ..., 6=Sunday)
        :param n: int (1=first, 2=second, ..., -1=last)
        :return: datetime.date
        """
        if n > 0:
            # Find the first day of the month
            first_day_of_month = datetime(year, month, 1)
            # Calculate the first specified weekday
            days_to_add = (weekday - first_day_of_month.weekday() + 7) % 7
            first_weekday = first_day_of_month + timedelta(days=days_to_add)
            # Calculate the nth specified weekday
            nth_weekday = first_weekday + timedelta(weeks=n-1)
        else:
            # Find the first day of the next month
            if month == 12:
                next_month = datetime(year + 1, 1, 1)
            else:
                next_month = datetime(year, month + 1, 1)
            # Go back one day to get the last day of the current month
            last_day_of_month = next_month - timedelta(days=1)
            # Calculate the last specified weekday
            days_to_go_back = (last_day_of_month.weekday() - weekday + 7) % 7
            nth_weekday = last_day_of_month - timedelta(days=days_to_go_back)
        return nth_weekday.date()

    def translate_service_date(self, service_date, year, month):
        """
        Translate the service_date indicator to an actual date.
        :param service_date: str (e.g., '-51' for last Sunday)
        :param year: int
        :param month: int
        :return: datetime.date
        """
        if service_date.startswith('-'):
            n = int(service_date[1])
            if service_date == '-91':
                return datetime(year, month, 1).date()
            elif service_date == '-99':
                if month == 12:
                    next_month = datetime(year + 1, 1, 1)
                else:
                    next_month = datetime(year, month + 1, 1)
                last_day_of_month = next_month - timedelta(days=1)
                return last_day_of_month.date()
            else:
                weekday = int(service_date[2])
                if n == 5:
                    return self.get_nth_weekday_of_month(year, month, weekday, -1)
                else:
                    return self.get_nth_weekday_of_month(year, month, weekday, n)
        else:
            # Handle regular dates
            return datetime.strptime(service_date, '%Y-%m-%d').date()

    def fetch_automatic_transactions(self, year, month):
        """
        Fetch and translate automatic transactions for the given month and year.
        :param year: int
        :param month: int
        :return: list of dict
        """
        self.connect()
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT * FROM automatic_transactions")
                rows = cursor.fetchall()
                transactions = []
                for row in rows:
                    transaction = {
                        'id': row[0],
                        'transaction_name': row[1],
                        'service_date': self.translate_service_date(row[2], year, month),
                        'amount': row[3],
                        'to_account': row[4],
                        'from_account': row[5],
                        'category': row[6]
                    }
                    transactions.append(transaction)
                return transactions
        except psycopg2.Error as e:
            print(f"Error fetching automatic transactions: {e}")
            return []
        finally:
            self.close()

    def check_persistent_state(self, state_key):
        """
        Check the persistent state for a given key.
        :param state_key: str
        :return: bool
        """
        self.connect()
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT state_value FROM persistent_state WHERE state_key = %s", (state_key,))
                result = cursor.fetchone()
                return result is not None and result[0] == 'true'
        except psycopg2.Error as e:
            print(f"Error checking persistent state: {e}")
            return False
        finally:
            self.close()

    def update_persistent_state(self, state_key, state_value):
        """
        Update the persistent state for a given key.
        :param state_key: str
        :param state_value: str
        """
        self.connect()
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO persistent_state (state_key, state_value, last_updated)
                    VALUES (%s, %s, CURRENT_TIMESTAMP)
                    ON CONFLICT (state_key) DO UPDATE
                    SET state_value = EXCLUDED.state_value, last_updated = EXCLUDED.last_updated
                """, (state_key, state_value))
                self.conn.commit()
        except psycopg2.Error as e:
            print(f"Error updating persistent state: {e}")
        finally:
            self.close()

    def append_automatic_transactions_to_qlog(self, year=None, month=None):
        """
        Append automatic transactions to the qlog table for the given month and year.
        :param year: int (default: current year)
        :param month: int (default: current month)
        """
        if year is None or month is None:
            now = datetime.now()
            year = now.year
            month = now.month

        state_key = f"auto_transactions_{year}_{month}"
        if self.check_persistent_state(state_key):
            print(f"Automatic transactions for {year}-{month} have already been appended.")
            return

        transactions = self.fetch_automatic_transactions(year, month)
        self.connect()
        try:
            with self.conn.cursor() as cursor:
                for transaction in transactions:
                    cursor.execute("""
                        INSERT INTO qlog (entry_date, entry_time, service_date, category, to_account, amount, from_account, status, comment, image, exec_time, deduction, t_code, distance)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (
                        datetime.now().date(), datetime.now().time(), transaction['service_date'], transaction['category'],
                        transaction['to_account'], transaction['amount'], transaction['from_account'], 'Pending', '',
                        None, datetime.now(), False, 'AUTO', None
                    ))
                self.conn.commit()
                self.update_persistent_state(state_key, 'true')
        except psycopg2.Error as e:
            print(f"Error appending automatic transactions to qlog: {e}")
        finally:
            self.close()