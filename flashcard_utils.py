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


def __input_text(field_name, error):
    while True:
        value = input(f'{field_name}:').strip()
        if not value:
            print(error)
            continue
        break
    return value


def all_cards_menu():
    flashcards = db.get_all(Flashcard)
    if not flashcards:
        print('There is no flashcard to practice!')
    else:
        yes_key = 'y'
        no_key = 'n'
        upd_key = 'u'
        menu = f'press "{yes_key}" to see the answer:\n' \
               f'press "{no_key}" to skip:\n' \
               f'press "{upd_key}" to update:'
        for card in flashcards:
            print(f'Question: {card.question}:')
            __show_menu(menu, {yes_key: lambda: __answer_menu(card),
                               upd_key: lambda: __update_card_menu(card),
                               no_key: None})


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


def __update_card_menu(card):
    del_key = 'd'
    edit_key = 'e'
    menu = f'press "{del_key}" to delete the flashcard:\n' \
           f'press "{edit_key}" to edit the flashcard:'
    __show_menu(menu, {del_key: lambda: delete(card),
                       edit_key: lambda: edit(card)})


def __answer_menu(card):
    yes_key = 'y'
    no_key = 'n'
    menu = f'press "{yes_key}" if your answer is correct:\n' \
           f'press "{no_key}" if your answer is wrong:'
    print(f'Answer: {card.answer}')
    __show_menu(menu, {yes_key: lambda: __if_yes(),
                       no_key: lambda: __if_no()})


def __if_yes():
    pass


def __if_no():
    pass
