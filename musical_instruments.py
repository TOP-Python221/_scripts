from abc import ABC, abstractmethod
from random import choice, randrange


class Instruments(ABC):
    """Абстрактный базовый класс для групп и семейств инструментов."""
    attack: float

    @abstractmethod
    def generate_sound(self):
        pass


class PickStrings(Instruments):
    """Класс семейства щипковых струнных инструментов."""
    attack: float = 1

    @abstractmethod
    def generate_sound(self):
        pass


class Guitar(PickStrings):
    """Класс инструмента акустической шестиструнной гитары"""
    tuning: tuple = ('e', 'B', 'G', 'D', 'A', 'E')
    tessitura: tuple = ('E-2', 'G2')

    @classmethod
    def generate_sound(cls):
        string = choice(cls.tuning)
        a, b = tuple(
            int(r[-2:]) if '-' in r else int(r[-1:])
            for r in cls.tessitura
        )
        pitch = randrange(a, b+1)
        print(f'Guitar {string}{pitch} picked')


class Harp(PickStrings):
    """Класс инструмента акустической арфы."""
    tessitura: tuple = ('C-2', 'G3')

    @classmethod
    def generate_sound(cls):
        string = choice('CDEFGAB')
        a, b = tuple(
            int(r[-2:]) if '-' in r else int(r[-1:])
            for r in cls.tessitura
        )
        pitch = randrange(a, b+1)
        print(f'Harp {string}{pitch} picked')


g1 = Guitar()
h1 = Harp()

for _ in range(20):
    choice((g1, h1)).generate_sound()
