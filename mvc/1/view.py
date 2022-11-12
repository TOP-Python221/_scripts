"""View (MVC): CLI представление."""

from time import sleep


def start_view():
    """Отображает приветствие."""
    print('\nДобро пожаловать в демонстратор MVC!')
    sleep(2)


def ask_view():
    """Отображает вопрос."""
    print('\nВывести все записи из БД? [y/n]')


def answer_view() -> str:
    """Получает и возвращает ответ."""
    return input(' > ')


def show_all(people: tuple):
    """Отображает всех людей построчно."""
    print(*people, sep='\n')
    sleep(10)


def end_view():
    """Отображает прощание."""
    print('\nПока!')
    sleep(2)
