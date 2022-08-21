
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'<Point: x={self.x}, y={self.y}>'

    def __str__(self):
        return f'({self.x}; {self.y})'

    def __eq__(self, other):
        """Проверяет на равенство объекты self и other.

        Вызывается при вычислении оператора == """
        if isinstance(other, Point):
            if self.x == other.x and self.y == other.y:
                return True
            else:
                return False
        else:
            raise TypeError('other object is not Point')

    def __lt__(self, other):
        """Проверяет меньше ли объект self, чем other.

        Вызывается при вычислении оператора < """
        if isinstance(other, Point):
            if self.x < other.x and self.y < other.y:
                return True
            else:
                return False
        else:
            raise TypeError('other object is not Point')

    def __gt__(self, other):
        """Проверяет больше ли объект self, чем other.

        Вызывается при вычислении оператора > """
        if isinstance(other, Point):
            if self.x > other.x and self.y > other.y:
                return True
            else:
                return False
        else:
            raise TypeError('other object is not Point')

    def __sub__(self, other):
        """Вычисляет расстояние между двумя точками."""
        if isinstance(other, Point):
            x2x1 = other.x - self.x
            y2y1 = other.y - self.y
            return round((x2x1**2 + y2y1**2)**0.5, 2)
        else:
            raise TypeError('other object is not Point')


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.length = self.end - self.start

    def __str__(self):
        return f"<Line: start={self.start!s}, " \
               f"end={self.end!s}, len={self.length}>"


p0 = Point(0, 0)
print(p0, end='\n\n')
print(repr(p0), end='\n\n')
print(f'{p0!r}\n{p0!s}', end='\n\n')

print(f'{p0 < Point(1, 1) = }')
print(f'{p0 > Point(1, -1) = }')
print(f'{p0 == Point(0, 1) = }\n')
# print(f'{p0 < 1 = }')


l1 = Line(start=p0, end=Point(2, 2))
print(l1)

