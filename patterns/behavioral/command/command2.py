"""Демонстратор Команды — групповая команда."""

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

    def __log(self, path_to_log: str | Path, cancel: bool = False):
        """Добавляет запись в журнал."""
        oper = self.action.name
        if cancel:
            oper = f'UNDO {oper}'
        out = f'{dt.now():%Y-%m-%d %H:%M:%S} - {self.account} - {oper} - {self.amount}\n'
        with open(path_to_log, 'a', encoding='utf-8') as f_out:
            f_out.write(out)

    def execute(self):
        """Выполняет и журналирует операцию."""
        if self.action is Operation.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action is Operation.WITHDRAW:
            self.success = self.account.withdraw(self.amount)
        else:
            raise TypeError
        if self.success:
            self.__log(log_path)

    def undo(self):
        """Отменяет операцию."""
        if self.success:
            if self.action is Operation.DEPOSIT:
                self.account.withdraw(self.amount)
            elif self.action is Operation.WITHDRAW:
                self.account.deposit(self.amount)
            self.__log(log_path, True)


class BankAccountCompositeCommand(Command, list):
    def __init__(self, *commands: Command):
        super().__init__()
        self.extend(commands)

    def execute(self):
        for command in self:
            command.execute()

    def undo(self):
        for command in reversed(self):
            command.undo()


ba = BankAccount(200)
print(f'Start {ba}\n')

comms = BankAccountCompositeCommand(
    BankAccountCommand(ba, Operation.DEPOSIT, 100),
    BankAccountCommand(ba, Operation.WITHDRAW, 1000),
    BankAccountCommand(ba, Operation.DEPOSIT, 50)
)
# comms.execute()
print(f'{ba}')
# comms.undo()
print(f'{ba}\n')


ba_from = BankAccount(250)
ba_to = BankAccount(10)
print(f'Start {ba_from = !s}, {ba_to = !s}')

transaction = BankAccountCompositeCommand(
    BankAccountCommand(ba_from, Operation.WITHDRAW, 1000),
    BankAccountCommand(ba_to, Operation.DEPOSIT, 1000)
)
transaction.execute()
print(f'{ba_from = !s}, {ba_to = !s}\n')
