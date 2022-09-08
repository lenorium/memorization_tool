import db
from models import Flashcard


def add_card():
    question = __input_text('Question', "The question can't be empty!")
    answer = __input_text('Answer', "The answer can't be empty!")
    db.save(Flashcard(question, answer))


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


def __input_text(field_name, error):
    while True:
        value = input(f'{field_name}:').strip()
        if not value:
            print(error)
            continue
        break
    return value
