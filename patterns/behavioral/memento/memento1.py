"""Шаблон проектирования: Хранитель — краткая реализация."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Memento:
    """Хранитель."""
    balance: int


class BankAccount:
    """Описывает основные операции с банковским счётом."""
    overdraft_limit = -500

    def __init__(self, start_balance: int = 0):
        self.__balance = start_balance

    def __str__(self):
        return f'balance: {self.__balance}'

    def deposit(self, amount: int) -> Memento:
        """Пополняет баланс счёта и сохраняет изменённый баланс в экземпляр Хранителя."""
        self.__balance += amount
        return Memento(self.__balance)

    def withdraw(self, amount: int) -> Optional[Memento]:
        """При допустимости операции производит снятие с баланса счёта и сохраняет изменённый баланс в экземпляр Хранителя."""
        if self.__balance - amount >= self.overdraft_limit:
            self.__balance -= amount
            return Memento(self.__balance)

    def restore(self, state: Memento) -> None:
        """Восстанавливает состояние счёта из экземпляра Хранителя."""
        self.__balance = state.balance


ba1 = BankAccount(150)
print('Start', ba1)

m1 = ba1.deposit(75)
print(ba1)
print(m1)

m2 = ba1.withdraw(190)
print(ba1)
print(m2)

m3 = ba1.deposit(220)
print(ba1)
m4 = ba1.deposit(15)
print(ba1)

ba1.restore(m1)
print(ba1)
