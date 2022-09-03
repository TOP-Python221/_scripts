from pprint import pprint


class Proteus:
    def move(self):
        print(f'{self.__class__.__name__} is moving')

    def reproduct(self):
        print(f'new {self.__class__.__name__} creature is born')
        return self.__class__()

class Fish(Proteus):
    def breath(self):
        print(f'{self.__class__.__name__} is breathing')

class Reptile(Fish):
    def hide(self):
        print(f'{self.__class__.__name__} is hiding')

class Bird(Reptile):
    def fly(self):
        print(f'{self.__class__.__name__} is flying')

class Mammals(Reptile):
    def care(self, who: str = ''):
        print(f'{self.__class__.__name__} is caring {who}')

    def reproduct(self):
        self.care('cubs')
        return self.__class__()

class Human(Mammals):
    def speak(self):
        print(f'{self.__class__.__name__} is speaking')


petya = Human()
pprint(petya.__class__.__mro__)

print('\n')

non_special_attrs = tuple(attr for attr in dir(petya) if not attr.startswith('__'))
pprint(non_special_attrs)

print('\n')

petya.move()
petya.breath()
petya.hide()
petya.care('only himself')
petya.speak()

