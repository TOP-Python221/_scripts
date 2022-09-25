"""Демонстратор фабрики: фабричный метод."""

from enum import Enum
from numbers import Real
from math import cos, sin, pi


class CoordinateSystem(Enum):
    CARTESIAN = 0
    POLAR = 1


class Point:
    # потенциально слишком крупный, неудобный и плохо масштабируемый конструктор
    # def __init__(self,
    #              a: Real,
    #              b: Real,
    #              system: CoordinateSystem = CoordinateSystem.CARTESIAN):
    #     if system is CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     elif system is CoordinateSystem.POLAR:
    #         self.x = round(a * cos(b), 2)
    #         self.y = round(a * sin(b), 2)

    def __init__(self, x: Real, y: Real):
        self.x = x
        self.y = y

    # фабричный метод
    @classmethod
    def new_cartesian(cls, x: Real, y: Real):
        return cls(x, y)

    # фабричный метод
    @classmethod
    def new_polar(cls, rho: Real, phi: Real):
        x = round(rho * cos(phi), 2)
        y = round(rho * sin(phi), 2)
        return cls(x, y)

    # фабричный метод
    # ...

    def __repr__(self):
        return f'<Point: x={self.x}, y={self.y}>'

    def __str__(self):
        return f'({self.x}; {self.y})'


p1 = Point(0, 0)
p2 = Point.new_cartesian(4, 5)
# p3 = Point(4, pi/2, CoordinateSystem.POLAR)
p3 = Point.new_polar(4, pi/2)
print(p1, p2, p3)
