from abc import ABC, abstractmethod
from enum import Enum
from random import choice
from typing import Optional


class Item(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @classmethod
    def random(cls):
        return choice(list(cls))


class Tie(Exception):
    pass


class Strategy(ABC):
    item: Item

    @staticmethod
    @abstractmethod
    def check(other: Item) -> bool:
        pass


class Rock(Strategy):
    item = Item.ROCK

    @staticmethod
    def check(other: Item) -> bool:
        if other is Item.SCISSORS:
            return True
        elif other is Item.PAPER:
            return False
        elif other is Item.ROCK:
            raise Tie


class Paper(Strategy):
    item = Item.PAPER

    @staticmethod
    def check(other: Item) -> bool:
        if other is Item.ROCK:
            return True
        elif other is Item.SCISSORS:
            return False
        elif other is Item.PAPER:
            raise Tie


class Scissors(Strategy):
    item = Item.SCISSORS

    @staticmethod
    def check(other: Item) -> bool:
        if other is Item.PAPER:
            return True
        elif other is Item.ROCK:
            return False
        elif other is Item.SCISSORS:
            raise Tie


class Random(Strategy):
    def __init__(self):
        self.item = Item.random()

    def check(self, other: Item) -> bool:
        if self.item is Item.ROCK:
            return Rock.check(other)
        elif self.item is Item.PAPER:
            return Paper.check(other)
        elif self.item is Item.SCISSORS:
            return Scissors.check(other)


class Player:
    def __init__(self, name: str, strategy: Optional[Item] = None):
        self.name = name
        self.change_strategy(strategy)

    def change_strategy(self, strategy: Optional[Item] = None):
        if strategy is None:
            self.strategy = Random()
        elif strategy is Item.ROCK:
            self.strategy = Rock()
        elif strategy is Item.PAPER:
            self.strategy = Paper()
        elif strategy is Item.SCISSORS:
            self.strategy = Scissors()

    def play(player1, player2: 'Player'):
        # print(f'{player1.name} {player1.strategy.item.name}')
        # print(f'{player2.name} {player2.strategy.item.name}')
        try:
            win = player1.strategy.check(player2.strategy.item)
            if win:
                # print(f'Победил {player1.name}')
                return True
            else:
                # print(f'Победил {player2.name}')
                return False
        except Tie:
            # print('Ничья')
            pass

    def __str__(self):
        return self.name


p1 = Player('Иван')
p2 = Player('Алла')

ROUNDS = 10**6

wins = 0
for _ in range(ROUNDS):
    p1.change_strategy()
    p2.change_strategy()
    if p1.play(p2):
        wins += 1
print(f"Процент побед при случайной стратегии: {wins/ROUNDS*100:.0f}%")

wins = 0
for _ in range(ROUNDS):
    p1.change_strategy(Item.PAPER)
    p2.change_strategy()
    if p1.play(p2):
        wins += 1
print(f"Процент побед при одной стратегии: {wins/ROUNDS*100:.0f}%")
