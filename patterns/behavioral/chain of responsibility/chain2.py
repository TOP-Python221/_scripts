"""Демонстратор цепочки ответственности: брокер обработчиков."""

from enum import Enum
from abc import ABC, abstractmethod


class Parameter(Enum):
    ATTACK = 0
    DEFENSE = 1


class Handlers(list):
    """Вызываемый список обработчиков."""
    def __call__(self, *args, **kwargs):
        for handler in self:
            handler(*args, **kwargs)
        # для отладчика
        pass


class Query:
    """Запрос, в котором вычисляются модифицируемые значения."""
    def __init__(self,
                 parameter: Parameter,
                 default_value: int):
        self.parameter = parameter
        self.value = default_value


class Game:
    """Брокер обработчиков."""
    def __init__(self):
        self.handlers = Handlers()

    def perform_query(self,
                      sender: 'Creature',
                      query: Query):
        self.handlers(sender, query)
        # для отладчика
        pass


class Creature:
    """Обрабатываемый объект."""
    def __init__(self,
                 game: Game,
                 name: str,
                 default_attack: int,
                 default_defense: int):
        self.game = game
        self.name = name.title()
        self.attack = default_attack
        self.defense = default_defense

    @property
    def final_attack(self):
        q = Query(Parameter.ATTACK, self.attack)
        self.game.perform_query(self, q)
        return q.value

    @property
    def final_defense(self):
        q = Query(Parameter.DEFENSE, self.defense)
        self.game.perform_query(self, q)
        return q.value

    def __str__(self):
        a = self.final_attack
        d = self.final_defense
        return f'{self.name}: A={a}, D={d}'


class CreatureModifier(ABC):
    """Абстрактный базовый класс для модификаторов."""
    def __init__(self, game: Game, creature: Creature):
        self.game = game
        self.creature = creature
        # во время создания объекта модификатора его обработчик автоматически добавляется в цепочку обработчиков
        self.game.handlers.append(self.handle)

    def remove_from_chain(self):
        """Удаляет обработчик модификатора из цепочки."""
        self.game.handlers.remove(self.handle)

    @abstractmethod
    def handle(self, sender: Creature, query: Query):
        pass


class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender: Creature, query: Query):
        if self.creature is sender:
            if query.parameter is Parameter.ATTACK:
                query.value *= 2


class IncreaseDefenseModifier(CreatureModifier):
    def handle(self, sender: Creature, query: Query):
        if self.creature is sender:
            if query.parameter is Parameter.DEFENSE:
                if self.creature.final_attack <= 2*query.value:
                    query.value += 1


new_game = Game()

goblin = Creature(new_game, 'strong goblin', 2, 2)
print(goblin)

bronze_spear = DoubleAttackModifier(new_game, goblin)
print(f'with spear {goblin}')

stilet = DoubleAttackModifier(new_game, goblin)
print(f'with stilet {goblin}')

helm = IncreaseDefenseModifier(new_game, goblin)
print(f'with helm {goblin}')

bronze_spear.remove_from_chain()
print(f'without spear {goblin}')
