from database.db_handler import DBHandler

class AppInitializer:
    def __init__(self, main_window, db_config):
        self.main_window = main_window
        self.db_config = db_config
        self.db_handler = DBHandler(db_config)

    def initialize(self):
        # Initialize the application (e.g., load initial data, set up UI)
        pass