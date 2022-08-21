class Rectangle:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        self.area = self.width * self.height



class Circle:
    def __init__(self, radius: int, circlength: int, area: int):
        self.rabius = radius
        self.circlenght = circlength
        self.area = area

r1 = Rectangle(20, 40)
print(r1.area)