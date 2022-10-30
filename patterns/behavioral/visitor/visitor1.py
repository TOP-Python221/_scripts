from abc import ABC
from dataclasses import dataclass


class Expression(ABC):
    """Описывает объекты математических выражений."""


@dataclass
class FloatExpression(Expression):
    value: float


@dataclass
class AdditionExpression(Expression):
    left: Expression
    right: Expression


class ExpressionPrinter:
    """Формирует строку для объекта выражения."""
    @classmethod
    def print(cls, buffer: list, expression: Expression):
        """Записывает в буфер строковое представление элементов выражения, осуществляя рекурсивный обход элементов выражения."""
        if type(expression) is FloatExpression:
            buffer += [str(expression.value)]
        elif type(expression) is AdditionExpression:
            buffer += ['(']
            cls.print(buffer, expression.left)
            buffer += [' + ']
            cls.print(buffer, expression.right)
            buffer += [')']
        else:
            raise NotImplementedError


expr = AdditionExpression(
    FloatExpression(1),
    AdditionExpression(
        FloatExpression(2),
        FloatExpression(3)
    )
)
# список expr_parts является посетителем
expr_parts = []
ExpressionPrinter.print(expr_parts, expr)
print(''.join(expr_parts))
