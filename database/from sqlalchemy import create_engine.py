from sqlalchemy import create_engine

db_url = 'postgresql://postgres:sasuke@localhost:5433/yukies_db'
engine = create_engine(db_url)

try:
    connection = engine.connect()
    print("Connection successful")
    connection.close()
except Exception as e:
    print(f"Connection failed: {e}")