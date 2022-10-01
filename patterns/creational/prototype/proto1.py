"""Демонстратор прототипа: ссылочная зависимость."""

from dataclasses import dataclass
from copy import deepcopy


@dataclass
class Address:
    city: str
    street: str
    building: str
    room: str

    def __str__(self):
        return f'{self.city}, {self.street} {self.building}-{self.room}'


@dataclass
class Person:
    name: str
    living_address: Address

    def __str__(self):
        return f'{self.name} живёт по адресу {self.living_address}'


ivan = Person('Иван', Address('Екатеринбург', 'пр. Космонавтов', '30Б', '202'))

liza = deepcopy(ivan)
liza.name = 'Лиза'
liza.living_address.room = '205'

print(ivan)
print(liza)
