from dataclasses import dataclass
from pprint import pprint


class Person_:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


@dataclass
class Person:
    name: str
    age: int
    address: str
    occupation: str


ivan = Person('Иван', 28)
pprint(Person.__dict__)
pprint(ivan.__dict__)
