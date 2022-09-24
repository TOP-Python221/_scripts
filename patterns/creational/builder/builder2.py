"""Демонстратор строителя: комбинированный строитель."""

class Person:
    def __init__(self, name: str):
        self.name = name
        self.street: str | None = None
        self.city: str | None = None
        self.postcode: str | None = None
        self.company: str | None = None
        self.position: str | None = None
        self.income: int | None = None

    def __str__(self):
        return f'{self.name} живёт по адресу: {self.postcode}, {self.city}, {self.street}, работает в компании {self.company} на позиции {self.position} зарабатывая в месяц {self.income} ₽'


class PersonBuilder:
    def __init__(self, person: Person = Person(input())):
        self.person = person

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    def build(self):
        return self.person


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person: Person):
        super().__init__(person)

    def at(self, street: str):
        self.person.street = street
        return self

    def in_city(self, city: str):
        self.person.city = city
        return self

    def with_postcode(self, postcode: str):
        self.person.postcode = postcode
        return self


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person: Person):
        super().__init__(person)

    def at(self, company: str):
        self.person.company = company
        return self

    def as_a(self, position: str):
        self.person.position = position
        return self

    def earns(self, income: int):
        self.person.income = income
        return self



pers1 = PersonBuilder()\
    .lives\
        .at('ул. Орджоникидзе 12')\
        .in_city('Екатеринбург')\
        .with_postcode('620012').\
    works\
        .at('Калина, ЗАО')\
        .as_a('Химик-технолог')\
        .earns(55000)\
    .build()

print(pers1)
