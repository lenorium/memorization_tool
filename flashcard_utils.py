import db
from models import Flashcard


def add_card():
    db.save(Flashcard(input('Question:'), input('Answer:')))


def practice():
    flashcards = db.get_all(Flashcard)
    if not flashcards:
        print('There is no flashcard to practice!')
    else:
        for card in flashcards:
            print(f'Question: {card.question}')
            show_answer = input('Please press "y" to see the answer or press "n" to skip:').lower().strip()
            if show_answer == 'y':
                print(f'Answer: {card.answer}')
