import os
from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Database URL environment variable from Heroku
DATABASE_URL = os.getenv('DATABASE_URL').replace("postgres://", "postgresql+psycopg2://", 1)  # Modify this line

# ... (rest of your code)

# Remove this line (let Alembic handle schema changes)
# Base.metadata.create_all(bind=engine) 

# ... (rest of your code)

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# FastAPI app instance
app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Example SQLAlchemy model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# Create the tables in the database
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Example route to get all users
@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


