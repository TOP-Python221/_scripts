"""Шаблон проектирования: Команда — """

from enum import Enum


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

    def withdraw(self, amount: int):
        if self.__balance - amount >= self.__class__.overdraft_limit:
            self.__balance -= amount
        else:
            pass


class BankAccountCommand:
    """Команда."""
    def __init__(self,
                 account: BankAccount,
                 action: Operation,
                 amount: int):
        self.addressee = account
        self.action = action
        self.amount = amount

    def execute(self):
        """Выполняет операцию."""
        if self.action is Operation.DEPOSIT:
            self.addressee.deposit(self.amount)
        elif self.action is Operation.WITHDRAW:
            self.addressee.withdraw(self.amount)
        else:
            raise TypeError

    def undo(self):
        """Отменяет операцию."""
        if self.action is Operation.DEPOSIT:
            self.addressee.withdraw(self.amount)
        elif self.action is Operation.WITHDRAW:
            self.addressee.deposit(self.amount)


# инициация команд
ba = BankAccount(100)
print(f'Start {ba}')

deposit1 = BankAccountCommand(ba, Operation.DEPOSIT, 50)
deposit1.execute()
print(ba)

deposit1.undo()
print(ba)
