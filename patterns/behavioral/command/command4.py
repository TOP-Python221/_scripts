"""Шаблон проектирования: Команда — полная инфраструктура, команды в разных классах."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime as dt


class ISwitchableDevices(ABC):
    """Абстрактный базовый класс адресатов."""
    @staticmethod
    @abstractmethod
    def turn_on():
        pass

    @staticmethod
    @abstractmethod
    def turn_off():
        pass


class Light(ISwitchableDevices):
    """Адресат."""
    @staticmethod
    def turn_on():
        print('Light is on')

    @staticmethod
    def turn_off():
        print('Light is off')


class ICommand(ABC):
    """Абстрактный базовый класс команд."""
    @abstractmethod
    def execute(self):
        pass


@dataclass
class SwitchOn(ICommand):
    """Команда на включение."""
    _receiver: ISwitchableDevices

    def execute(self):
        self._receiver.turn_on()


@dataclass
class SwitchOff(ICommand):
    """Команда на выключение."""
    _receiver: ISwitchableDevices

    def execute(self):
        self._receiver.turn_off()


class Switch:
    """Инициатор."""
    def __init__(self):
        self._commands: dict[str, ICommand] = {}
        self._history: list[tuple[dt, str]] = []

    def register(self, command_name: str, command: ICommand):
        self._commands[command_name] = command

    def execute(self, command_name: str):
        if command_name in self._commands:
            self._commands[command_name].execute()
            self._history.append((dt.now(), command_name))
        else:
            raise

    def show_history(self):
        pass

    def replay_last(self, number: int = 1):
        if number <= len(self._history):
            for i in range(-1, -number-1, -1):
                entry = self._history[i]
                command_name = entry[1]
                self.execute(command_name)



torcher = Light()

smart_switch = Switch()
smart_switch.register('ON', SwitchOn(torcher))
smart_switch.register('OFF', SwitchOff(torcher))

smart_switch.execute('ON')
smart_switch.execute('OFF')

smart_switch.replay_last()
