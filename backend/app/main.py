from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from . import models, schemas, crud, auth, database
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    full_name: str | None = None
    profile_pic: str | None = None

class QuizCreate(BaseModel):
    course_id: int
    date_taken: str
    score: int
    recommended_topics: list

class QuestionCreate(BaseModel):
    topic_id: int
    question_text: str
    difficulty: str
    choice_a: str
    choice_b: str
    choice_c: str
    choice_d: str
    correct_answer: str
    explanation: str

@app.post("/token", response_model=auth.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(SessionLocal)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=schemas.User)
def create_user(user: UserCreate, db: Session = Depends(SessionLocal)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/profile", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(auth.get_current_user)):
    return current_user

@app.post("/quizzes/", response_model=schemas.Quiz)
async def create_quiz(quiz: QuizCreate, db: Session = Depends(SessionLocal)):
    db_quiz = models.Quiz(
        user_id=quiz.user_id,
        course_id=quiz.course_id,
        date_taken=quiz.date_taken,
        score=quiz.score,
        recommended_topics=json.dumps(quiz.recommended_topics)
    )
    db.add(db_quiz)
    db.commit()
    db.refresh(db_quiz)
    return db_quiz

@app.post("/questions/", response_model=schemas.Question)
async def create_question(question: QuestionCreate, db: Session = Depends(SessionLocal)):
    db_question = models.Question(
        topic_id=question.topic_id,
        question_text=question.question_text,
        difficulty=question.difficulty,
        choice_a=question.choice_a,
        choice_b=question.choice_b,
        choice_c=question.choice_c,
        choice_d=question.choice_d,
        correct_answer=question.correct_answer,
        explanation=question.explanation
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question
