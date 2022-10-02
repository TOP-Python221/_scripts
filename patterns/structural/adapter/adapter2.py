"""Демонстратор адаптера: подмена имён методов."""
from pprint import pprint


class Cat:
    @staticmethod
    def meow():
        return 'мяу'

class Dog:
    @staticmethod
    def bark():
        return 'гав'

class Human:
    @staticmethod
    def speak():
        return 'привет'

class Car:
    @staticmethod
    def move(speed: int = 60):
        return 'вр' + 'у'*(speed//20) + 'м'


class Adapter:
    def __init__(self, obj, **methods):
        self.obj = obj
        self.__dict__ |= methods

    def __getattr__(self, item):
        return getattr(self.obj, item)


# адаптируемые объекты
cat = Cat()
dog = Dog()
guy = Human()
car = Car()

# адаптированные объекты
cat_adapted = Adapter(cat, make_noise=cat.meow)
dog_adapted = Adapter(dog, make_noise=dog.bark)
guy_adapted = Adapter(guy, make_noise=guy.speak)
car_adapted = Adapter(car, make_noise=car.move)

def without_dunder(names: list[str]):
    return [name
            for name in names
            if not (name.startswith('__') and name.endswith('__'))]

# сравнение областей видимости адаптируемых и адаптированных
pprint(without_dunder(dir(cat)))
pprint(without_dunder(dir(cat_adapted)))
print()
pprint(without_dunder(dir(dog)))
pprint(without_dunder(dir(dog_adapted)))
print()
print(cat_adapted.make_noise())
print(dog_adapted.make_noise(), end='\n\n')

# пакетная обработка адаптированных объектов
for creature in (cat_adapted, dog_adapted, guy_adapted, car_adapted):
    print(creature.make_noise())

# также, можем получить доступ к области видимости адаптируемого объекта
print(cat_adapted.meow())
