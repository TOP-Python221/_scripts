import math


class Rectangle:
    def __init__(self, height: int, widght: int,):
        self.widght = widght
        self.height = height

    def area(self):
        return self.widght * self.height

r1 = Rectangle(15, 43)
print(r1.area())


class Circle:
    def __init__(self, rad: int):
        self.rad = rad

    def area(self):
        return math.pi * (self.rad ** 2)

    def len_Circle(self):
        return 2 * math.pi * self.rad


r2 = Circle(16)
print(r2.area())
print()
print(r2.len_Circle())
