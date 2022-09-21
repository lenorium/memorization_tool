import flashcard_utils
from models import Flashcard
import random


def navigate(menu_item):
    while True:
        print(menu_item)
        while True:
            command = input()
            if command not in menu_item.submenu:
                print(f'\n{command} is not an option')
                print(menu_item)
                continue
            break
        choice = menu_item.submenu[command]
        if choice.action:
            choice.action()
            if menu_item is MenuItem.main_menu():
                continue
            else:
                break
        if choice.submenu:
            navigate(choice)
        else:
            break


def practice_menu():
    max_stage = flashcard_utils.get_max_box()
    current_stage = 0

    while current_stage <= max_stage:
        print(f'Level {current_stage + 1}')
        flashcards = flashcard_utils.get_all_cards(lambda: Flashcard.box <= current_stage)
        random.shuffle(flashcards)

        for card in flashcards:
            print(f'Question: {card.question}\n')
            key = input('Press "Enter" to see answer or "s" to skip ')
            if key != 's':
                flashcard_utils.check_answer(card)
            if __exit_command():
                return
        current_stage += 1


def update_menu():
    flashcards = flashcard_utils.get_all_cards()
    if not flashcards:
        print('There is no flashcards')
    else:
        menu = MenuItem(submenu={
            '1': MenuItem(name='Edit the flashcard', action=lambda: flashcard_utils.edit(card)),
            '2': MenuItem(name='Delete the flashcard', action=lambda: flashcard_utils.delete(card)),
            '3': MenuItem('Skip')
        })
        for card in flashcards:
            print(f'Question: {card.question}\n')
            navigate(menu)
            if __exit_command():
                break


def __exit_command():
    to_exit = input(f'\nType "exit" to quit practice mode ').lower().strip() == 'exit'
    print()
    return to_exit


def add_menu():
    key = None
    while key != 'n':
        flashcard_utils.add()
        print()
        key = input('Press "n" for quit or any key for continue ').lower().strip()


class MenuItem:
    __main_menu = None

    def __init__(self, name=None, submenu=None, action=None):
        self.__name = name
        self.__submenu = submenu if submenu is not None else {}
        self.__action = action

    @property
    def name(self):
        return self.__name

    @property
    def submenu(self):
        return self.__submenu

    @property
    def action(self):
        return self.__action

    def __str__(self):
        return '\n'.join(f'{key}. {val.__name}' for key, val in self.__submenu.items())

    def __repr__(self):
        return f'{self.__name} <{id(self)}>'

    @classmethod
    def __create_menu(cls):
        return MenuItem(submenu={
            '1': MenuItem('Practice flashcards', action=practice_menu),
            '2': MenuItem('Add flashcard', action=add_menu),
            '3': MenuItem('Update flashcards', action=update_menu),
            '4': MenuItem('Exit')})

    @classmethod
    def main_menu(cls):
        if cls.__main_menu is None:
            cls.__main_menu = cls.__create_menu()
        return cls.__main_menu
