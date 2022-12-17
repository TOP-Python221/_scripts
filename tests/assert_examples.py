import re

from dataclasses import dataclass
from json import load as jload
from pathlib import Path
from string import ascii_lowercase, whitespace
from sys import path


class A:
    def __init__(self):
        self.data = input(' > ').lower().strip()

    @staticmethod
    def valid_input(data: str):
        return set(data) <= set(ascii_lowercase) | set(whitespace)


a = A()

assert a.valid_input(a.data), 'string should contain only latin letters and space characters'
print("тест 1 пройден")

assert 2 < len(a.data) < 10, 'length of string should be between 3 and 9 characters'
print("тест 2 пройден")



people_file = Path(path[0]) / 'people.json'

@dataclass
class Person:
    name: str
    age: int
    email: str
    phone: str
    country: str
    langs: list[str]

    def __str__(self):
        return self.name

    @staticmethod
    def get_all() -> tuple['Person', ...]:
        with open(people_file, encoding='utf-8') as filein:
            people = jload(filein)
        result = ()
        for person in people:
            person['langs'] = person['langs'].split()
            result += (Person(**person), )
        return result


email_pattern = re.compile(r'[a-zA-Z0-9]*@[a-zA-Z]*\.[a-zA-Z]{2,3}')
phone_pattern = re.compile(r'\+7(?P<sep>[ -]?)9\d\d(?P=sep)\d{3}(?P=sep)\d{4}')

people = Person.get_all()
for pers in people:
    try:
        assert email_pattern.fullmatch(pers.email), 'email'
        assert phone_pattern.fullmatch(pers.phone), 'phone'
        print(f'correct data: {pers.name}')
    except AssertionError as ae:
        print(f'wrong {ae}: {pers.name}')
