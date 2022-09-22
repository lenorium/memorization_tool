import os

from sqlalchemy import create_engine
from  sqlalchemy.sql.functions import max
from sqlalchemy.orm import sessionmaker
from models import Base

# db_url = os.getenv('db_url')
# db_url = 'sqlite:///:memory:'
db_url = 'sqlite:///flashcard.db'
engine = create_engine(db_url, echo=True)
Base.metadata.create_all(engine)
session_maker = sessionmaker(bind=engine)


def save(entity):
    try:
        with session_maker.begin() as session:
            session.add(entity)
    except Exception as e:
        print(e)


def get_all(cls, *filter_exp):
    with session_maker() as session:
        return session.query(cls).filter(*filter_exp).all()


def delete(entity):
    try:
        with session_maker.begin() as session:
            session.delete(entity)
    except Exception as e:
        print(e)


def get_max(col):
    with session_maker() as session:
        return session.query(max(col)).one()