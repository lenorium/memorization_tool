import flashcard_utils


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
    flashcards = flashcard_utils.get_all_cards()

    for card in flashcards:
        print(f'Question: {card.question}\n')
        input('Press "Enter" to see answer')
        flashcard_utils.check_answer(card)
        to_exit = input('Type "exit" to quit practice mode: ').lower().strip() == 'exit'
        if to_exit:
            break


def update_menu():
    flashcards = flashcard_utils.get_all_cards()

    menu = MenuItem(submenu={
        '1': MenuItem(name='Edit the flashcard', action=lambda: flashcard_utils.edit(card)),
        '2': MenuItem(name='Delete the flashcard', action=lambda: flashcard_utils.delete(card)),
        '3': MenuItem('Skip')
    })
    for card in flashcards:
        print(f'Question: {card.question}\n')
        navigate(menu)


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
