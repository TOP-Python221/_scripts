"""Dependencies Inversion Principle — Принцип Инверсии Зависимостей"""

from dataclasses import dataclass
from enum import Enum


class Relation(Enum):
    PARENT = 0
    CHILD = 1


@dataclass
class Person:
    name: str
    def __str__(self):
        return f'<Person: {self.name}>'


# нарушение принцип инверсии зависимостей: отсутствие средств, которые могут быть использованы кодом верхнего уровня для того, чтобы не использовать низкоуровневую реализацию хранилища
class Relationships:
    def __init__(self):
        # хранилище
        self.storage = []

    def add_relation(self, parent: Person, child: Person):
        self.storage += [
            (parent, Relation.PARENT, child),
            (child, Relation.CHILD, parent)
        ]


steve = Person('Steve')
kate = Person('Kate')
george = Person('George')
elen = Person('Elen')
alice = Person('Alice')
kit = Person('Kit')

db = Relationships()
db.add_relation(steve, george)
db.add_relation(steve, elen)
db.add_relation(kate, george)
db.add_relation(kate, elen)
db.add_relation(george, alice)
