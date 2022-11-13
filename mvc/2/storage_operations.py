"""CRUD операции с хранилищем данных."""

from decimal import Decimal as dec
from pprint import pprint

from storage_exceptions import *

# хранилище
__items: list[dict] = []
# [{'name': str, 'price': dec, 'quantity': int}, ...]


def create_items(items_list: list[dict]):
    """Добавляет несколько элементов в хранилище."""
    global __items
    intersection = set(item['name'] for item in __items) & \
                   set(item['name'] for item in items_list)
    if not intersection:
        __items.extend(items_list)
    else:
        raise ItemAlreadyStoredError(tuple(intersection)[0])


def create_item(name: str, price: str, quantity: int):
    """Добавляет один элемент в хранилище."""
    global __items
    if not tuple(filter(
        lambda item: item['name'] == name,
        __items
    )):
        __items.append({'name': name, 'price': dec(price), 'quantity': quantity})
    else:
        raise ItemAlreadyStoredError(name)


def read_items():
    """Возвращает все элементы из хранилища в виде полной несвязанной копии."""
    global __items
    return [item.copy() for item in __items]


def read_item(name: str) -> dict:
    """Возвращает элемент из хранилища по имени."""
    global __items
    result = tuple(filter(
        lambda item: item['name'] == name,
        __items
    ))
    if result:
        return result[0]
    else:
        raise ItemNotStoredError(name)


def update_item(name: str, /, *, price: str = None, quantity: int = None):
    """Обновляет поля 'цена' и/или 'количество' для элемента в хранилище."""
    global __items
    if price is None and quantity is None:
        raise TypeError('update_item() should take at least one key argument')
    result = tuple(
        (i, item)
        for i, item in enumerate(__items)
        if item['name'] == name
    )
    if result:
        i, item = result[0]
        __items[i] = {
            'name': name,
            'price': item['price'] if price is None else price,
            'quantity': item['quantity'] if quantity is None else quantity
        }
    else:
        raise ItemNotStoredError(name)


def delete_item(name: str):
    """Удаляет элемент из хранилища по имени."""
    global __items
    result = tuple(filter(
        lambda item: item['name'] == name,
        __items
    ))
    if result:
        __items.remove(result[0])
    else:
        raise ItemNotStoredError(name)


__goods = [
    {'name': 'Хлеб', 'price': '36.22', 'quantity': 8},
    {'name': 'Молоко', 'price': '91.80', 'quantity': 11},
    {'name': 'Шоколад', 'price': '158.00', 'quantity': 5},
]
create_items(__goods)


# тесты
if __name__ == '__main__':
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
