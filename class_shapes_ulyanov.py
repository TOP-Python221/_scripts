PI = 3.14
class Rectangle:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        self.area = self.width * self.height



class Circle:
    def __init__(self, radius: int):
        self.radius = radius
        self.area = PI * self.radius ** 2
        self.circlelengs = 2 * PI * self.radius ** 2

c1 = Circle(12)
print(f'площадь круга = {c1.area}, длина окружности = {c1.circlelengs}')
r1 = Rectangle(20, 40)
print(r1.area)