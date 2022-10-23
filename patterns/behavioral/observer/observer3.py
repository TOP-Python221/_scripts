"""Демонстратор наблюдателя: вызываемый список наблюдателей."""

from dataclasses import dataclass


class Observers(list):
    """Вызываемый список наблюдателей."""
    def __call__(self, *args, **kwargs):
        for observer in self:
            # вызов наблюдателя
            observer(*args, **kwargs)


@dataclass
class Person:
    """Субъект наблюдения."""
    name: str
    address: str

    def __post_init__(self):
        # список наблюдателей
        self.falls_ill = Observers()

    def catch_cold(self):
        """Событие."""
        self.falls_ill(self.name, self.address)


def call_doctor(name: str, address: str):
    """Наблюдатель."""
    print(f'{name} нуждается в докторе по адресу {address}')


inna = Person('Инна', 'г. Екатеринбург, ул. Первомайская 70, кв. 120')
# подписка наблюдателей
inna.falls_ill.append(
    # наблюдатель
    lambda name, address: print(f'{name} заболела')
)
inna.falls_ill.append(call_doctor)

# генерация события
inna.catch_cold()
