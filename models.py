from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Flashcard(Base):
    __tablename__ = 'flashcard'

    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String, nullable=False, unique=True)
    answer = Column(String, nullable=False)

    def __init__(self, question, answer):
        super().__init__()
        self.question = question
        self.answer = answer
