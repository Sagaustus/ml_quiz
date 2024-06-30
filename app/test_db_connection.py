import os
from sqlalchemy import create_engine

DATABASE_URL = os.getenv('DATABASE_URL').replace("postgres://", "postgresql+psycopg2://", 1)
print(f"DATABASE_URL: {DATABASE_URL}")  # Print the URL for debugging

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")
