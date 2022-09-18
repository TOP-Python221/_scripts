"""Liskov Substitution Principle — Принцип Подстановки Лисков."""

class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = value

    @property
    def area(self):
        return self._height * self._width


class Square(Rectangle):
    def __init__(self, size: int):
        super().__init__(size, size)

    # нарушает принцип подстановки Лисков
    @Rectangle.width.setter
    def width(self, value: int):
        self._width = value
        self._height = value

    # нарушает принцип подстановки Лисков
    @Rectangle.height.setter
    def height(self, value: int):
        self._width = value
        self._height = value


def high_level_function(rect: Rectangle):
    width = rect.width
    rect.height = 10
    expected_area = width * 10
    print(f'Ожидаемая площадь: {expected_area}\n'
          f'Рассчитанная площадь: {rect.area}')


r1 = Rectangle(5, 7)
print(f'{r1.area = }')

sq1 = Square(9)
sq2 = Rectangle(9, 9)
print(f'{sq1.area = }')

print('\nr1:')
high_level_function(r1)
print('\nsq1')
high_level_function(sq1)
print()


