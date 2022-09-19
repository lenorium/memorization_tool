import db
from models import Flashcard


def add():
    question = __input_text('Question', "The question can't be empty!")
    answer = __input_text('Answer', "The answer can't be empty!")
    db.save(Flashcard(question, answer))


def delete(card):
    db.delete(card)


def edit(card):
    print(f'current question: {card.question}')
    question = input('please write a new question: ')

    print(f'current answer: {card.answer}')
    answer = input('please write a new answer: ')

    card.question = question
    card.answer = answer
    db.save(card)


def __show_menu(menu: str, actions: dict):
    while True:
        menu_item = input(menu).lower().strip()
        if menu_item not in actions.keys():
            print(f'\n{menu_item} is not an option')
        else:
            action = actions[menu_item]
            if action:
                action()
            break


def get_action():
    flashcards = db.get_all(Flashcard)
    if not flashcards:
        print('There is no flashcard to practice!')
    else:
        menu = 'press "y" to see the answer:\n' \
               'press "n" to skip:\n' \
               'press "u" to update:'
        for card in flashcards:
            print(f'Question: {card.question}:')
            __show_menu(menu, {'y': lambda: print(f'Answer: {card.answer}'),
                               'u': lambda: __update_card(card),
                               'n': None})


def __update_card(card):
    menu = 'press "d" to delete the flashcard:\n' \
           'press "e" to edit the flashcard:\n'
    __show_menu(menu, {'d': lambda: delete(card),
                       'e': lambda: edit(card)})


def __input_text(field_name, error):
    while True:
        value = input(f'{field_name}:').strip()
        if not value:
            print(error)
            continue
        break
    return value
