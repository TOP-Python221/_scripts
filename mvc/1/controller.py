"""Controller (MVC): управляющий модуль, точка входа."""
from time import sleep

import model
# import view
import view_gui as view


def start():
    """Вызывает начальное представление."""
    view.start_view()
    ask()


def ask():
    """Вызывает представление с вопросом и вводом ответа."""
    view.ask_view()
    validate_answer()


def validate_answer():
    """Проверяет корректность строки с ответом."""
    while True:
        answer = view.answer_view()
        if answer in ('y', 'д', 'n', 'н'):
            break
    process_answer(answer)


def process_answer(string: str):
    """Проверяет положительный ответ."""
    if string in ('y', 'д'):
        get_people()
    end()


def get_people():
    """Получает данные из модели и передаёт представлению."""
    people = model.Person.get_all()
    view.show_all(people)


def end():
    """Вызывает завершающее представление."""
    view.end_view()


# точка входа
if __name__ == '__main__':
    start()
