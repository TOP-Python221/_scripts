from math import pi, sqrt


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    @property
    def length(self) -> float:
        return 2 * pi * self.radius

    @length.setter
    def length(self, new_length: float) -> None:
        self.radius = new_length / (2 * pi)

    @property
    def area(self) -> float:
        return pi * self.radius**2

    @area.setter
    def area(self, new_area: float) -> None:
        self.radius = sqrt(new_area / pi)


c1 = Circle(5)
print(f'{c1.radius = }\n{c1.length = }\n{c1.area = }\n')

c1.length = 15.7
print(f'{c1.radius = }\n{c1.length = }\n{c1.area = }\n')

c1.area = 100
print(f'{c1.radius = }\n{c1.length = }\n{c1.area = }\n')
