from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import QuizQuestion, QuizResponse
from .ml_model import recommend_topics
from .database import SessionLocal, engine, Base

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

