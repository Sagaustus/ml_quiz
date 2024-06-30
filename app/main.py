import os
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import QuizQuestion, QuizResponse
from .ml_model import recommend_topics
from .database import SessionLocal, engine, Base

# Database URL environment variable from Heroku
DATABASE_URL = os.getenv('DATABASE_URL').replace("postgres://", "postgresql+psycopg2://", 1)  # Modify this line


# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()



# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to get all quiz questions
@app.get("/quiz/")
def read_quiz(db: Session = Depends(get_db)):
    questions = db.query(QuizQuestion).all()
    return questions

# Endpoint to submit a quiz response
@app.post("/quiz/response/")
def submit_response(response: QuizResponse, db: Session = Depends(get_db)):
    db.add(response)
    db.commit()
    db.refresh(response)
    return response

# Endpoint to get recommendations based on quiz performance

@app.get("/recommendations/")
def get_recommendations(db: Session = Depends(get_db)):
    responses = db.query(QuizResponse).all()
    recommendations = recommend_topics(responses)
    return recommendations




