from functools import lru_cache
from math import pi


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    @property
    def area(self) -> float:
        return pi * self.radius**2

    @property
    def length(self) -> float:
        return 2 * pi * self.radius


class Circle2:
    def __init__(self, radius: float):
        self.radius = radius
        self.length = 2 * pi * self.radius
        self.area = pi * self.radius**2


circle = Circle(5)
print(f'{circle.length = :.2f}\t{circle.area = :.2f}')
circle.radius = 7
print(f'{circle.length = :.2f}\t{circle.area = :.2f}')
