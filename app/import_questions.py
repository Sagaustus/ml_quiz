import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, QuizQuestion

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def load_questions(csv_file):
    session = SessionLocal()
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            question = QuizQuestion(
                question_text=row['question_text'],
                correct_answer=row['correct_answer'],
                category=row['category']
            )
            session.add(question)
        session.commit()

if __name__ == "__main__":
    load_questions('questions.csv')
