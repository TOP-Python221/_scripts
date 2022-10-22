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

    def __repr__(self):
        result = (f"<{self.name}:"
                  f" POS=({self.position['x']};{self.position['y']}),"
                  f" LVL={self.level},"
                  f" HP={self.health}>")
        for item in self.inventory:
            result += f'\n\t{item}'
        return result

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
            print('\nИГРА ОКОНЧЕНА\n')

    def level_up(self) -> None:
        self.level += 1

    def pick_item(self, item: str) -> None:
        self.inventory += [item.lower()]

    def drop_item(self, item: str) -> None:
        item = item.lower()
        if item in self.inventory:
            self.inventory.remove(item)

    @property
    def state(self) -> CharacterState:
        """"""
        return CharacterState(
            self.level,
            self.health,
            self.position.copy(),
            self.inventory.copy()
        )

    @state.setter
    def state(self, save: CharacterState) -> None:
        """"""
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



hero = Character('Дюк')
print(repr(hero))

menu = SaveLoadMenu(hero)

hero.move(1, 0)
hero.pick_item('пистолет')
hero.move(2, 0)
hero.hit()
hero.hit()
hero.level_up()
hero.move(-2, 1)
print(repr(hero))

menu.save()

hero.move(0, 2)
hero.pick_item('нож')
hero.move()
hero.hit()
hero.hit()
hero.hit()
hero.drop_item('пистолет')
hero.move(3, -4)
print(repr(hero))

menu.save()

hero.move()
hero.pick_item('патроны к винтовке')
hero.move(0, 1)
hero.hit()
hero.hit()
hero.hit()
hero.hit()
hero.hit()
hero.hit()
print(repr(hero))

menu.load()

print(repr(hero))
