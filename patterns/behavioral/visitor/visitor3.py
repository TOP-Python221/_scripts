from abc import ABC
from dataclasses import dataclass
from typing import Callable, Type


_methods = {}

def assign_type(expression_type: Type['Expression']) -> Callable:
    """Определяет объект класса, с которым должен работать декорируемый метод."""

    def type_method_mapper(method_object: Callable) -> Callable:
        """Сохраняет декорируемый метод в словарь по ключу. Ключом является имя класса объекта, с которым работает метод."""
        _methods[expression_type.__name__] = method_object

        def _wrapper(instance_object: 'ExpressionPrinter', expression: 'Expression') -> None:
            """Получает из словаря нужный метод в зависимости от класса объекта, с которым должен работать метод."""
            method = _methods[expression.__class__.__name__]
            return method(instance_object, expression)

        return _wrapper

    return type_method_mapper


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
    """Посетитель — формирует строку для объекта выражения"""
    def __init__(self):
        self.buffer: list[str] = []

    def __str__(self):
        return ''.join(self.buffer)

    @assign_type(FloatExpression)
    def visit(self, expression: FloatExpression):
        self.buffer += [str(expression.value)]

    @assign_type(AdditionExpression)
    def visit(self, expression: AdditionExpression):
        self.buffer += ['(']
        self.visit(expression.left)
        self.buffer += [' + ']
        self.visit(expression.right)
        self.buffer += [')']



expr = AdditionExpression(
    FloatExpression(1),
    AdditionExpression(
        FloatExpression(2),
        FloatExpression(3)
    )
)
ep = ExpressionPrinter()
ep.visit(expr)
print(ep)
