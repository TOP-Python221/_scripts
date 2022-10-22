"""Шаблон проектирования: Хранитель — реализация фиксированной истории изменений."""

from dataclasses import dataclass


@dataclass
class Memento:
    """Хранитель."""
    balance: int


class FixedList(list):
    """Список с ограничением максимального количества элементов."""
    def __init__(self, list_length: int):
        super().__init__()
        self.length = list_length

    def append(self, __object) -> None:
        """При достижении максимального количества элементов удаляет первый элемент и добавляет новый."""
        if len(self) == self.length:
            self.pop(0)
        super().append(__object)


class BankAccount:
    """Описывает основные операции с банковским счётом."""
    overdraft_limit = -500
    history_length = 5

    def __init__(self, start_balance: int = 0):
        self.__balance = start_balance
        # история изменений фиксированной длины
        self.__history: FixedList[Memento] = FixedList(self.history_length)
        self.__history.append(Memento(self.__balance))
        # индекс текущего состояния
        self._index: int = 0

    def __str__(self):
        return f'balance: {self.__balance}'

    def deposit(self, amount: int):
        """Пополняет баланс счёта, сохраняет изменённый баланс в экземпляр Хранителя и инкрементирует индекс текущего состояния."""
        self.__balance += amount
        self.__history.append(Memento(self.__balance))
        if self._index < self.history_length - 1:
            self._index += 1

    def withdraw(self, amount: int):
        """При допустимости операции производит снятие с баланса счёта, сохраняет изменённый баланс в экземпляр Хранителя и инкрементирует индекс текущего состояния."""
        if self.__balance - amount >= self.overdraft_limit:
            self.__balance -= amount
            self.__history.append(Memento(self.__balance))
            if self._index < self.history_length - 1:
                self._index += 1

    def show_history(self) -> str:
        """Возвращает строку с историей изменений."""
        return '\n'.join(repr(state) for state in self.__history)

    def undo(self) -> None:
        """Восстанавливает предыдущее состояние в истории изменений."""
        if self._index > 0:
            self._index -= 1
            self.__balance = self.__history[self._index].balance

    def redo(self) -> None:
        """Восстанавливает следующее состояние в истории изменений."""
        if self._index < len(self.__history) - 1:
            self._index += 1
            self.__balance = self.__history[self._index].balance


ba1 = BankAccount(40)
ba1.deposit(50)
ba1.withdraw(310)
ba1.deposit(230)
ba1.deposit(120)
print(ba1.show_history(), end='\n'*2)

ba1.deposit(1000)
print(ba1.show_history(), end='\n'*2)

ba1.undo()
print(ba1)
ba1.undo()
print(ba1)
ba1.undo()
print(ba1)
ba1.undo()
print(ba1)
# без изменений
ba1.undo()
print(ba1, end='\n'*2)

ba1.redo()
print(ba1)
ba1.redo()
print(ba1)
ba1.redo()
print(ba1)
ba1.redo()
print(ba1)
# без изменений
ba1.redo()
print(ba1, end='\n'*2)
