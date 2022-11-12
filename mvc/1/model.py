"""Model (MVC): модель данных."""

from pathlib import Path
from sys import path

from dataclasses import dataclass
from json import load as jload

from typing import Literal

people_file = Path(path[0]) / 'people.json'

LangCodes = Literal['RU', 'EN', 'FR', 'IT', 'SP', 'DE', 'CH', 'KZ', 'JP']

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

    def does_speak(self, lang: LangCodes) -> bool:
        return lang in self.langs



if __name__ == '__main__':
    data = Person.get_all()
    print(*data[:10], sep='\n', end='\n\n')

    for pers in data:
        if pers.does_speak('KZ'):
            print(pers)

