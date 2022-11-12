"""Controller (MVC): управляющий модуль, точка входа."""

import model
import view


def start():
    """Вызывает начальное представление."""
    view.start_view()
    ask()


def ask():
    """Вызывает представление с вопросом и вводом ответа."""
    view.ask_view()
    while True:
        answer = view.answer_view()
        if validate_answer(answer):
            break
    if process_answer(answer):
        get_people()
    end()


def validate_answer(string: str) -> bool:
    """Проверяет корректность строки с ответом."""
    return string in ('y', 'д', 'n', 'н')


def process_answer(string: str) -> bool:
    """Проверяет положительный ответ."""
    return string in ('y', 'д')


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
