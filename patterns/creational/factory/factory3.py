"""Демонстратор фабрики: классы фабрик."""

from numbers import Real
from math import cos, sin, pi


class Point:
    def __init__(self, x: Real, y: Real):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'<Point: x={self.x}, y={self.y}>'

    def __str__(self):
        return f'({self.x}; {self.y})'

    @staticmethod
    def create():
        return PointFactory()


class PointFactory:
    @property
    def cartesian(self):
        return PointFactoryCartesian.new_cartesian

    @property
    def polar(self):
        return PointFactoryPolar.new_polar


class PointFactoryCartesian:
    @staticmethod
    def new_cartesian(x: Real, y: Real):
        """Создаёт объект точки, используя декартову систему координат.

        :param x: координата по оси абсцисс
        :param y: координата по оси ординат
        """
        return Point(x, y)


class PointFactoryPolar:
    @staticmethod
    def new_polar(rho: Real, phi: Real):
        """Создаёт объект точки, используя полярную систему координат.

        :param rho: длина радиус-вектора
        :param phi: тангенциальный угол
        """
        x = round(rho * cos(phi), 2)
        y = round(rho * sin(phi), 2)
        return Point(x, y)


p1 = Point.create().cartesian(0, 0)
p2 = Point.create().polar(2, pi/6)
print(p1, p2)
