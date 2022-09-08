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
        if choice.submenu:
            navigate(choice)
        elif choice.action:
            choice.action()
        else:
            break


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
            '1': MenuItem('Add flashcards', {
                '1': MenuItem('Add a new flashcard', action=flashcard_utils.add_card),
                '2': MenuItem('Exit')}),
            '2': MenuItem('Practice flashcards', action=flashcard_utils.practice),
            '3': MenuItem('Exit')})

    @classmethod
    def get_menu(cls):
        if cls.__main_menu is None:
            cls.__main_menu = cls.__create_menu()
        return cls.__main_menu
