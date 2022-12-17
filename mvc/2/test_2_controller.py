from decimal import Decimal as dec

import storage_operations as so
from application import Model, View, Controller


so.items = [
    {'name': 'Хлеб', 'price': dec('36.22'), 'quantity': 8},
    {'name': 'Молоко', 'price': dec('91.80'), 'quantity': 11},
    {'name': 'Шоколад', 'price': dec('158.00'), 'quantity': 5},
]


class TestDMOperations:
    c = Controller(None, View())
    c.model = Model()

    def test_insert(self):
        item = {
            'name': 'Курица тушка',
            'price': '509.90',
            'quantity': 8
        }
        self.c.insert_item(**item)
        assert any(map(
            lambda obj: obj['name'] == item['name']
                        and obj['price'] == dec(item['price'])
                        and obj['quantity'] == item['quantity'],
            so.items
        ))

    def test_update(self):
        item = {
            'name': 'Молоко',
            'price': '85.20',
            'quantity': 11
        }
        self.c.update_item(
            item['name'],
            new_price=item['price'],
            new_quantity=item['quantity'],
        )
        assert any(map(
            lambda obj: obj['name'] == item['name']
                        and obj['price'] == dec(item['price'])
                        and obj['quantity'] == item['quantity'],
            so.items
        ))

