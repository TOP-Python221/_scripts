"""Пользовательские исключения для операция с хранилищем."""


class ItemAlreadyStoredError(Exception):
    def __init__(self, item_name: str):
        super().__init__(f'item {item_name!r} is already stored')


class ItemNotStoredError(Exception):
    def __init__(self, item_name: str):
        super().__init__(f'item {item_name!r} is not stored')
