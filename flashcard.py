class Flashcard:
    __flashcards = []

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    @classmethod
    def add_card(cls):
        cls.__flashcards.append(Flashcard(input('Question:'), input('Answer:')))

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

