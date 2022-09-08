import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# db_url = os.getenv('db_url')
# db_url = 'sqlite:///:memory:'
db_url = 'sqlite:///flashcard.db'
engine = create_engine(db_url, echo=True)
Base.metadata.create_all(engine)
session_maker = sessionmaker(bind=engine)


def save(entity):
    with session_maker() as session:
        session.add(entity)
        session.commit()


def get_all(cls):
    with session_maker() as session:
        return session.query(cls).all()
