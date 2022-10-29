from numbers import Real
from typing import Callable

from operator import add, sub, mul, truediv


class Calculator:
    def __init__(self, number1: Real, number2: Real):
        self.number1 = number1
        self.number2 = number2

    def calc(self, operation: Callable):
        return operation(self.number1, self.number2)


c1 = Calculator(1, 3)

print(c1.calc(add))
print(c1.calc(sub))
print(c1.calc(mul))
print(c1.calc(truediv), end='\n\n')

print(c1.calc(print))
print(c1.calc(Calculator))
