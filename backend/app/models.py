from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean, JSON, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String, index=True)
    profile_pic = Column(String, nullable=True)
    quizzes = relationship("Quiz", back_populates="user")

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

class Topic(Base):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey('courses.id', ondelete='CASCADE'))
    name = Column(String, nullable=False)
    course = relationship("Course", back_populates="topics")
    questions = relationship("Question", back_populates="topic")

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(Integer, ForeignKey('topics.id', ondelete='CASCADE'))
    question_text = Column(Text, nullable=False)
    difficulty = Column(String, nullable=True)
    choice_a = Column(Text, nullable=False)
    choice_b = Column(Text, nullable=False)
    choice_c = Column(Text, nullable=False)
    choice_d = Column(Text, nullable=False)
    correct_answer = Column(String(1), nullable=False)
    explanation = Column(Text, nullable=True)
    topic = relationship("Topic", back_populates="questions")

class Quiz(Base):
    __tablename__ = 'quizzes'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    course_id = Column(Integer, ForeignKey('courses.id', ondelete='CASCADE'))
    date_taken = Column(TIMESTAMP, nullable=False)
    score = Column(Integer, nullable=False)
    recommended_topics = Column(JSON, nullable=True)
    user = relationship("User", back_populates="quizzes")
    course = relationship("Course")

class UserResponse(Base):
    __tablename__ = 'user_responses'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    question_id = Column(Integer, ForeignKey('questions.id', ondelete='CASCADE'))
    user_answer = Column(String(1), nullable=False)
    is_correct = Column(Boolean, nullable=False)
    user = relationship("User")
    question = relationship("Question")
