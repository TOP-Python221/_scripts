"""CRUD операции с хранилищем данных."""

from decimal import Decimal as dec
from pprint import pprint

from storage_exceptions import *

# хранилище
items: list[dict] = []
# [{'name': str, 'price': dec, 'quantity': int}, ...]


def create_items(items_list: list[dict]):
    """Добавляет несколько элементов в список."""
    global items
    intersection = set(item['name'] for item in items) & \
                   set(item['name'] for item in items_list)
    if not intersection:
        items.extend(items_list)
    else:
        raise ItemAlreadyStoredError(tuple(intersection)[0])


def create_item(name: str, price: str, quantity: int):
    """Добавляет один элемент в список."""
    global items
    if price == '':
        raise ValueError('price takes an empty string')
    if not tuple(filter(
        lambda item: item['name'] == name,
        items
    )):
        items.append({'name': name, 'price': dec(price), 'quantity': quantity})
    else:
        raise ItemAlreadyStoredError(name)


def read_items() -> list[dict]:
    """Возвращает все элементы из списка в виде полной несвязанной копии."""
    global items
    return [item.copy() for item in items]


def read_item(name: str) -> dict:
    """Возвращает один элемент из списка по имени."""
    global items
    result = tuple(filter(
        lambda item: item['name'] == name,
        items
    ))
    if result:
        return result[0]
    else:
        raise ItemNotStoredError(name)


def update_item(name: str, /, *, price: str = None, quantity: int = None):
    """Обновляет поля 'цена' и/или 'количество' для одного элемента в списке."""
    global items
    if price is None and quantity is None:
        raise TypeError('update_item() should take at least one key argument')
    if price == '':
        raise ValueError('price takes an empty string')
    result = tuple(
        (i, item)
        for i, item in enumerate(items)
        if item['name'] == name
    )
    if result:
        i, item = result[0]
        items[i] = {
            'name': name,
            'price': item['price'] if price is None else dec(price),
            'quantity': item['quantity'] if quantity is None else quantity
        }
    else:
        raise ItemNotStoredError(name)


def delete_item(name: str):
    """Удаляет один элемент из списка по имени."""
    global items
    result = tuple(filter(
        lambda item: item['name'] == name,
        items
    ))
    if result:
        items.remove(result[0])
    else:
        raise ItemNotStoredError(name)


# тесты
if __name__ == '__main__':
    __goods = [
        {'name': 'Хлеб', 'price': '36.22', 'quantity': 8},
        {'name': 'Молоко', 'price': '91.80', 'quantity': 11},
        {'name': 'Шоколад', 'price': '158.00', 'quantity': 5},
    ]
    create_items(__goods)
    pprint(read_items())

    print()

    update_item('Хлеб', quantity=5)
    update_item('Молоко', price='90.20')
    update_item('Шоколад', price='147.50', quantity=10)
    pprint(read_items())

    print()

    delete_item('Шоколад')
    pprint(read_items())

    print()

    update_item('Хлеб', quantity=0)
    update_item('Хлеб', price='')
    pprint(read_items())

    print()
