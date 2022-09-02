class Flashcard:
    __flashcards = []

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    @classmethod
    def add_card(cls):
        question = cls.__input_text('Question', "The question can't be empty!")
        answer = cls.__input_text('Answer', "The answer can't be empty!")
        cls.__flashcards.append(Flashcard(question, answer))

    @classmethod
    def practice(cls):
        if not len(cls.__flashcards):
            print('There is no flashcard to practice!')
        else:
            for card in cls.__flashcards:
                print(f'Question: {card.question}')
                show_answer = input('Please press "y" to see the answer or press "n" to skip:').lower().strip()
                if show_answer == 'y':
                    print(f'Answer: {card.answer}')

    @staticmethod
    def __input_text(field_name, error):
        while True:
            value = input(f'{field_name}:').strip()
            if not value:
                print(error)
                continue
            break
        return value
