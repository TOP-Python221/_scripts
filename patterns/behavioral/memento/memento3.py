"""Шаблон проектирования: Хранитель — полная инфраструктура."""

from dataclasses import dataclass, field


@dataclass
class CharacterState:
    """Состояние персонажа.

    Хранитель (memento)
    """
    level: int
    health: int
    position: dict[str, int]
    inventory: list[str]

    def __str__(self):
        return (f"POS=({self.position['x']};{self.position['y']}),"
                f" LVL={self.level},"
                f" HP={self.health}")


@dataclass
class Character:
    """Персонаж игры.

    Инициатор (originator)
    """
    name: str
    level: int = 1
    health: int = 10
    inventory: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.name = self.name.title()
        self.dead: bool = False
        self.position: dict[str, int] = {'x': 0, 'y': 0}

    def __str__(self):
        return self.name

    def move(self, delta_x: int = 1, delta_y: int = 1) -> None:
        self.position['x'] += delta_x
        self.position['y'] += delta_y

    def hit(self) -> None:
        if self.health > 0:
            self.health -= 1
        else:
            self.dead = True

    def level_up(self) -> None:
        self.level += 1

    def pick_item(self, item: str) -> None:
        self.inventory += [item]

    def drop_item(self, item: str) -> None:
        if item in self.inventory:
            self.inventory.remove(item)

    @property
    def state(self) -> CharacterState:
        return CharacterState(
            self.level,
            self.health,
            self.position,
            self.inventory
        )

    @state.setter
    def state(self, save: CharacterState) -> None:
        self.level = save.level
        self.health = save.health
        self.position = save.position
        self.inventory = save.inventory


class SaveLoadMenu:
    """Управляет сохранением и загрузкой игры.

    Опекун (caretaker)
    """
    def __init__(self, character: Character):
        self.character = character
        self.__saves: list[CharacterState] = []

    def _show_saves(self) -> None:
        """"""
        print(f'\nСписок сохранений для персонажа {self.character}')
        for i, save in enumerate(self.__saves, 1):
            print(f'\t{i}. {save}')

    def _get_save_slot(self) -> int:
        """"""
        while True:
            inp = input(' > введите номер слота для загрузки: ')
            if inp.isdecimal():
                inp = int(inp)
                if 1 <= inp <= len(self.__saves):
                    return inp
                else:
                    print(' ... введите номер существующего слота ... ')
            else:
                print(' ... введите число ... ')

    def save(self) -> None:
        """"""
        self.__saves += [self.character.state]

    def load(self):
        """"""
        self._show_saves()
        i = self._get_save_slot() - 1
        self.character.state = self.__saves[i]


