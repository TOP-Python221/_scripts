"""Демонстратор фабрики: выбирающая фабрика."""

from dataclasses import dataclass
from datetime import datetime as dt
from random import choice


@dataclass
class Person:
    name: str
    birthdate: dt

    def __str__(self):
        return f'{self.name}: {self.birthdate:%d.%m.%Y}'


@dataclass
class Employee(Person):
    position: str = None
    income: int = None

    def __str__(self):
        return super().__str__() \
               + f', {self.position} ({self.income})'


@dataclass
class Candidate(Person):
    cv: bytes = None
    expert1: bool = False
    expert2: bool = False
    head: bool = False

    def tech_meeting1(self):
        self.expert1 = choice((False, True))

    def tech_meeting2(self):
        self.expert2 = choice((False, True))

    def final_meeting(self):
        self.head = choice((
            False,
            all((self.expert1, self.expert2))
        ))

    def __str__(self):
        return super().__str__() \
               + f', {self.expert1}/{self.expert2}/{self.head}'


class Factory:
    def __init__(self, age_min: int = 18, age_max: int = 56):
        self.age_min = age_min
        self.age_max = age_max

    @staticmethod
    def create_candidate(name: str, birthdate: str):
        q = Candidate(
            name=name,
            birthdate=dt.strptime(birthdate, '%d.%m.%Y')
        )
        # with open('cv.pdf', 'rb') as f_in:
        #     q.cv = f_in.read()
        return q

    def hire_candidate(self, person: Candidate, position: str, income: int):
        age = (dt.now() - person.birthdate).days // 365
        if self.age_min <= age <= self.age_max:
            if all([person.expert1, person.expert2, person.head]):
                q = Employee(
                    person.name,
                    person.birthdate,
                    position=position,
                    income=income
                )
                return q
        return person


hr_department = Factory()

dmitry = hr_department.create_candidate('Дмитрий', '05.05.1987')
print(dmitry)

dmitry.tech_meeting1()
dmitry.tech_meeting2()
dmitry.final_meeting()

dmitry = hr_department.hire_candidate(dmitry, 'Оператор баз данных', 58590)
print(dmitry)
