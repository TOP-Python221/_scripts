from abc import ABC
from decimal import Decimal as D
from numbers import Real


class Item(ABC):
    __id: int = 0

    def __init__(self, price: int | str):
        self.price = D(price)
        self.__class__.__id += 1
        self.__id = self.__class__.__id

    def __hash__(self):
        return self.__id

    def return_price(self):
        return f'{self.price} ₽'


class Smartphone(Item):
    pass

class Charger(Item):
    pass

class Earphones(Item):
    pass


coupons = {
    'IDL55MRR5YP': D('0.02'),
    'JXQ87QCA3QJ': D('0.07'),
    'BYU25ECM2PC': D('0.05'),
    'DXE44WIC9KB': D('0.10'),
    'QQP62TBN3EM': D('0.05')
}


class Box(dict):
    def __init__(self, items: dict[Item, int]):
        super().__init__()
        self.update(items)
        self.coupons: set = set()

    def apply_coupon(self, coupon: str):
        self.coupons.add(coupon)

    def return_price(self) -> str:
        price = 0
        for item, amount in self.items():
            price += item.price * amount
        discount = sum(coupons.get(coup, 0) for coup in self.coupons)
        price = price*(1 - discount)
        return f'{price} ₽'


phone = Smartphone(52500)
print('Стоимость смартфона без аксессуаров:', phone.return_price())

package = Box({
    phone: 1,
    Charger(1350): 2,
    Earphones(7220): 1
})
print('Стоимость смартфона с аксессуарами:', package.return_price())
package.apply_coupon('JXQ87QCA3QJ')
print('Стоимость смартфона с аксессуарами после скидки:', package.return_price())
package.apply_coupon('BYU25ECM2PC')
print('Стоимость смартфона с аксессуарами после второй скидки:', package.return_price())
