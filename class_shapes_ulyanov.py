import math

class Rectangle:
    def __init__(self, height: int, width: int, name: str):
        self.name = name
        self.height = height
        self.width = width
        self.area = self.width * self.height

    def __str__(self):
        return f'площадь прямоугольника {self.name} = {self.area}'
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            if self.area == other.area:
                return f'<{self} равна {other}'
            else:
                return f'<{self} не равна {other}'
    def __lt__(self, other):
         if isinstance(other, Rectangle):
            if self.area < other.area:
                return f'<{self} меньше чем {other}'
            else:
                return f'<{self} больше либо равна {other}'

class Circle:
    def __init__(self, radius: int, name: str):
        self.name = name
        self.radius = radius
        # вычисление площади
        self.area = math.pi * self.radius ** 2
        # вычисление длины окружности
        self.circlelengs = 2 * math.pi * self.radius ** 2

    def __str__(self):
        return f'площадь круга = {self.area:.2f}\nдлина окружности = {self.circlelengs:.2f}'

    def __repr__(self):
        return f'<{self.name}: длинна окружносити = {self.circlelengs:.2f}\n     площадь круга = {self.area:.2f}'

c1 = Circle(12, 'c1')
c2 = Circle(5, 'c2')
r1 = Rectangle(50, 40, 'r1')
r2 = Rectangle(60, 80, 'r2')

print(r1)
print(repr(c1))
print(repr(c2))
print(r1 < r2)
print(r1 == r2)