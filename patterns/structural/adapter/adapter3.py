"""Демонстратор адаптера: реализация отображения отрезка."""
from math import sqrt
from numbers import Real


# мы должны использовать эту реализацию отображения точки
def draw_point(point):
    return '.'


class Point:
    def __init__(self, x: Real, y: Real):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return f'({self.x:.1f}; {self.y:.1f})'


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def __repr__(self):
        return f'<Line: start={self.start} end={self.end}>'

    def length(self) -> float:
        x1, x2 = self.start.x, self.end.x
        y1, y2 = self.start.y, self.end.y
        return sqrt((x1 - x2)**2 + (y1 - y2)**2)


# y1 = k*x1 + b
# y2 = k*x2 + b
# b = y1 - k*x1
# y2 = k*x2 - k*x1 + y1
# k = (y2 - y1)/(x2 - x1)

class PointsInLine(list):
    """Формирует список из точек для отрезка, заданного двумя точками."""
    def __init__(self, line: Line, scale: Real = 1):
        super().__init__()

        self.append(line.start)

        x1, y1 = line.start.x, line.start.y
        x2, y2 = line.end.x, line.end.y
        try:
            k = (y2 - y1)/(x2 - x1)
        except ZeroDivisionError:
            k = float('inf')
        b = y1 - k*x1

        for xn in range(1, int((x2 - x1)/scale)):
            dx = x1 + xn*scale
            dy = k*dx + b
            self.append(Point(dx, dy))

        self.append(line.end)

    def __repr__(self):
        return '\n'.join(str(p) for p in self)

    def __str__(self):
        return ''.join(draw_point(p) for p in self)


p0 = Point(0, 0)
print(draw_point(p0))

l1 = Line(p0, Point(3, 7))
# для отрезка не получается корректным образом использовать имеющуюся реализацию отображения точки
print(draw_point(l1.start), draw_point(l1.end), sep='', end='\n\n')

l1_points = PointsInLine(l1, 0.5)
print(f'{l1_points!r}')
print(f'{l1_points!s}\n\n')



class Rectangle(list):
    def __init__(self, point1: Point, point2: Point, point3: Point):
        super().__init__()
        point4 = Point(point3.x, point1.y)
        l1 = Line(point1, point2)
        l2 = Line(point2, point3)
        l3 = Line(point3, point4)
        l4 = Line(point4, point1)
        if l1.length() == l3.length() and l2.length() == l4.length():
            self.append(l1)
            self.append(l2)
            self.append(l3)
            self.append(l4)
        else:
            raise ValueError("couldn't construct a rectangle with these points")


rc1 = Rectangle(
    Point(1, 1),
    Point(1, 4),
    Point(4, 4),
)
for side in rc1:
    print(f'{side!r}')
print()

for side in rc1:
    side = PointsInLine(side)
    print(f'{side!r}\n')
print()
