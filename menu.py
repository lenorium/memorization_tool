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
            if menu_item is MenuItem.get_menu():
                continue
            else:
                break
        if choice.submenu:
            navigate(choice)
        else:
            break


def cards_menu():
    flashcards = flashcard_utils.get_all_cards()

    menu = MenuItem(submenu={
        '1': MenuItem(name='See the answer', action=lambda: flashcard_utils.check_answer(card)),
        '2': MenuItem(name='Skip'),
        '3': MenuItem(name='Update', submenu={
            '1': MenuItem(name='Delete the flashcard', action=lambda: flashcard_utils.delete(card)),
            '2': MenuItem(name='Edit the flashcard', action=lambda: flashcard_utils.edit(card)),
            '3': MenuItem('Exit')
        }),
        '4': MenuItem(name='Exit'),
    })
    for card in flashcards:
        print(f'Question: {card.question}\n')
        navigate(menu)


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
                '1': MenuItem('Add a new flashcard', action=flashcard_utils.add),
                '2': MenuItem('Exit')}),
            '2': MenuItem('Practice flashcards', action=cards_menu),
            '3': MenuItem('Exit')})

    def __add_cards_menu(self):
        cards = flashcard_utils.get_all_cards()
        for card in cards:
            self.__submenu = MenuItem(submenu={
                '1': MenuItem(name='See the answer', action=lambda: flashcard_utils.check_answer(card)),
                '2': MenuItem(name='Skip'),
                '3': MenuItem(name='Update', submenu={
                    '1': MenuItem(name='Delete the flashcard', action=lambda: flashcard_utils.delete(card)),
                    '2': MenuItem(name='Edit the flashcard', action=lambda: flashcard_utils.edit(card)),
                    '3': MenuItem('Exit')
                }),
                '4': MenuItem(name='Exit'),
            })

    @classmethod
    def get_menu(cls):
        if cls.__main_menu is None:
            cls.__main_menu = cls.__create_menu()
        return cls.__main_menu
