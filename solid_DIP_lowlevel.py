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


class Relationships:
    def __init__(self):
        # хранилище
        self.storage = []

    def add_relation(self, parent: Person, child: Person):
        self.storage += [
            (parent, Relation.PARENT, child),
            (child, Relation.CHILD, parent)
        ]

    def find_all_children(self, name: str):
        for entry in self.storage:
            if entry[0].name.lower() == name.lower():
                if entry[1] is Relation.PARENT:
                    yield entry[2]


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
