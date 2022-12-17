from decimal import Decimal as dec

import storage_operations as so
from application import Model


def test_create_item():
    item = {
        'name': 'Chicken',
        'price': '509.90',
        'quantity': 8
    }
    Model.create_item(**item)
    assert any(map(
        lambda obj: obj['name'] == item['name']
                    and obj['price'] == dec(item['price'])
                    and obj['quantity'] == item['quantity'],
        so.items
    ))
