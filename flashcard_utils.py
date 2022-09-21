import db
from models import Flashcard


def add():
    question = __input_text('Question', "The question can't be empty!")
    answer = __input_text('Answer', "The answer can't be empty!")
    db.save(Flashcard(question, answer))


def delete(card):
    db.delete(card)


def edit(card):
    print(f'Current question: {card.question}')

    is_edited = False
    question = input('Please write a new question or press "Enter" to skip: ')
    if question:
        card.question = question
        is_edited = True

    print(f'\nCurrent answer: {card.answer}')
    answer = input('Please write a new answer or press "Enter" to skip: ')
    if answer:
        card.answer = answer
        is_edited = True

    if is_edited:
        db.save(card)


def __input_text(field_name, error):
    while True:
        value = input(f'{field_name}:').strip()
        if not value:
            print(error)
            continue
        break
    return value


def get_all_cards(filter_exp=None):
    return db.get_all_by_filter(Flashcard, filter_exp) if filter_exp else db.get_all(Flashcard)


def get_max_box():
    max_box = db.get_max(Flashcard.box)
    return max_box[0] if max_box else 0


def check_answer(card):
    print(f'Answer: {card.answer}')
    is_correct = input('Is your answer correct? press "y" for "yes" and "n" for "no": ')
    if is_correct:
        __is_correct_answer(card)
    else:
        __is_wrong_answer(card)


def __is_correct_answer(card: Flashcard):
    if card.is_in_max_box():
        db.delete(card)
    else:
        card.box += 1
        db.save(card)


def __is_wrong_answer(card: Flashcard):
    if not card.is_in_min_box():
        card.box -= 1
        db.save(card)
