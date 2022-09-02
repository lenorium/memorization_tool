import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# db_url = os.getenv('db_url')
db_url = 'sqlite:///:memory:'
engine = create_engine(db_url, echo=True)
Base.metadata.create_all(engine)
session_maker = sessionmaker(bind=engine)
session = session_maker()


def save(entity):
    session.add(entity)
    session.commit()


def get_all(cls):
    return session.query(cls).all()
