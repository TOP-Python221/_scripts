class Vehicle:
    definition = 'a mechanism that can move'

    def __init__(self, wheels: int | None):
        self.wheels = wheels

    def move(self):
        print(f'{self.__class__.__name__} is moving')


class Bicycle(Vehicle):
    pass

class Car(Vehicle):
    pass

class Train(Vehicle):
    definition = 'a mechanism that can move, but only within railroads'

class Helicopter(Vehicle):
    def move(self):
        print(f'{self.__class__.__name__} is flying fast')

    def move_parent(self):
        super().move()


v = Vehicle(None)
v.type = 'land'

bic = Bicycle(2)
car = Car(4)
trn = Train(12)
hel = Helicopter(0)

for v in (bic, car, trn, hel):
    print(f'\n{v.__class__.__name__} has {v.wheels} wheels')
    v.move()

print()
hel.move_parent()

print(f"\n{bic.definition = }")
print(f"{trn.definition = }")

