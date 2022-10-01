"""Демонстратор прототипа: реализация для объектной модели."""

from dataclasses import dataclass, field
from abc import ABC
from copy import deepcopy


@dataclass
class Unit(ABC):
    health: int = 10
    attack: int = 5
    defense: int = 3
    morale: int = 0

    def clone(self):
        return deepcopy(self)


@dataclass
class Longspear(Unit):
    speed: int = 5


@dataclass
class Monk(Unit):
    mana: int = 7


@dataclass
class Merchant(Unit):
    charisma: int = 3


@dataclass
class Hero:
    name: str
    class_: str
    level: int = 1
    army: list[Unit] = field(default_factory=list, init=False)

    def __post_init__(self):
        self.__class__.longs_proto = Longspear(12, 5, 3, 1)
        self.__class__.monk_proto = Monk(9, 7, 1, 2)
        self.__class__.merch_proto = Merchant(10, 0, 2, 0)

    def hire_army(self,
                  longspears_amount: int,
                  monks_amount: int = 0,
                  merchants_amount: int = 0):
        for _ in range(longspears_amount):
            self.army += [self.__class__.longs_proto.clone()]
        for _ in range(monks_amount):
            self.army += [self.__class__.monk_proto.clone()]
        for _ in range(merchants_amount):
            self.army += [self.__class__.merch_proto.clone()]

    def __str__(self):
        return f'{self.name.title()}: {self.class_} {self.level} ур.\n' \
               + '\n'.join(f'\t{unit}' for unit in self.army)



zig = Hero('Зигфрид', 'Рыцарь-элементалист')
print(zig)

zig.hire_army(10, 4, 1)
print(zig)
