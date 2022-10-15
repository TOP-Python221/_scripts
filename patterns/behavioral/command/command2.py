"""Шаблон проектирования: Команда — групповая команда."""

from enum import Enum
from pathlib import Path
from sys import path
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime as dt

SCRIPT_DIR = Path(path[0])
log_path = SCRIPT_DIR / 'operations.log'

class Operation(Enum):
    DEPOSIT = 0
    WITHDRAW = 1


class BankAccount:
    """Адресат команд."""
    overdraft_limit = -500

    def __init__(self, start_balance: int = 0):
        self.__balance = start_balance

    def __str__(self):
        return f'balance: {self.__balance}'

    def deposit(self, amount: int):
        self.__balance += amount

    def withdraw(self, amount: int) -> bool:
        if self.__balance - amount >= self.__class__.overdraft_limit:
            self.__balance -= amount
            return True
        else:
            return False


class Command(ABC):
    """Абстрактный базовый класс команд."""
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


@dataclass
class BankAccountCommand(Command):
    account: BankAccount
    action: Operation
    amount: int
    success: bool = field(default_factory=bool, init=False)

    def execute(self):
        """Выполняет и журналирует операцию."""
        if self.action is Operation.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action is Operation.WITHDRAW:
            self.success = self.account.withdraw(self.amount)
        else:
            raise TypeError

    def undo(self):
        """Отменяет операцию."""
        if self.success:
            if self.action is Operation.DEPOSIT:
                self.account.withdraw(self.amount)
            elif self.action is Operation.WITHDRAW:
                self.account.deposit(self.amount)


class BankAccountCompositeCommand(Command, list):
    def __init__(self):
        pass

    def execute(self):
        pass

    def undo(self):
        pass
