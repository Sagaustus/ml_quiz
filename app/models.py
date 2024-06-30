from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.main import Base

class QuizQuestion(Base):
    __tablename__ = 'quiz_questions'
    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True)
    correct_answer = Column(String)
    category = Column(String)

class QuizResponse(Base):
    __tablename__ = 'quiz_responses'
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey('quiz_questions.id'))
    selected_answer = Column(String)
    is_correct = Column(Integer)

    question = relationship("QuizQuestion", back_populates="responses")

QuizQuestion.responses = relationship("QuizResponse", order_by=QuizResponse.id, back_populates="question")
