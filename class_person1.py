import re
from datetime import datetime as dt

class Person:
    def __init__(self,
                 name: str,
                 surname: str,
                 birthdate: str):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

    @property
    def birthdate(self):
        raise NameError('access denied')

    @birthdate.setter
    def birthdate(self, value: str) -> None:
        if re.match(r'[12][09]\d\d-[01]\d-[0123]\d', value):
            self._birthdate = dt.strptime(value, '%Y-%m-%d').date()

    @property
    def age(self):
        return (dt.now().date() - self._birthdate).days // 365


candidate1 = Person('Kot', 'Kotovich', '2000-06-20')
candidate2 = Person('Pes', 'Psovich', '01.03.2010')

print(f'\n{candidate1.age = }')
print(f'\n{candidate2.age = }\n')
