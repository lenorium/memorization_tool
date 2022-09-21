from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Flashcard(Base):
    __tablename__ = 'flashcard'

    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    box = Column(Integer, name='box', nullable=False)

    def __init__(self, question, answer):
        super().__init__()
        self.question = question
        self.answer = answer
        self.box = 0

    __MAX_BOX = 2

    # @hybrid_property
    # @property
    # def box(self) -> int:
    #     return self.__box
    #
    # @box.setter
    # def box(self, box: int):
    #     if 0 > box > self.__MAX_BOX:
    #         print(f'"box" must be in range from 0 to {self.__MAX_BOX}')
    #     self.__box = box

    def is_in_max_box(self) -> bool:
        return self.box == self.__MAX_BOX

    def is_in_min_box(self) -> bool:
        return self.box == 0