"""Шаблон проектирования: Команда — """

from enum import Enum
from pathlib import Path
from sys import path
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


class BankAccountCommand:
    """Команда."""
    def __init__(self,
                 account: BankAccount,
                 action: Operation,
                 amount: int):
        self.addressee = account
        self.action = action
        self.amount = amount
        self.success = False

    def execute(self):
        """Выполняет и журналирует операцию."""
        if self.action is Operation.DEPOSIT:
            self.addressee.deposit(self.amount)
            self.success = True
        elif self.action is Operation.WITHDRAW:
            self.success = self.addressee.withdraw(self.amount)
        else:
            raise TypeError
        if self.success:
            self.__log(log_path)

    def __log(self, path_to_log: str | Path, cancel: bool = False):
        """Добавляет запись в журнал."""
        oper = self.action.name
        if cancel:
            oper = f'UNDO {oper}'
        out = f'{dt.now():%Y-%m-%d %H:%M:%S} - {self.addressee} - {oper} - {self.amount}\n'
        with open(path_to_log, 'a', encoding='utf-8') as f_out:
            f_out.write(out)

    def undo(self):
        """Отменяет операцию."""
        if self.success:
            if self.action is Operation.DEPOSIT:
                self.addressee.withdraw(self.amount)
            elif self.action is Operation.WITHDRAW:
                self.addressee.deposit(self.amount)
            self.__log(log_path, True)


# инициация команд
ba = BankAccount(100)
print(f'Start {ba}\n')

deposit1 = BankAccountCommand(ba, Operation.DEPOSIT, 50)
deposit1.execute()
print(ba)

deposit1.undo()
print(ba, end='\n\n')

withdraw1 = BankAccountCommand(ba, Operation.WITHDRAW, 1000)
withdraw1.execute()
print(ba)

withdraw1.undo()
print(ba)
