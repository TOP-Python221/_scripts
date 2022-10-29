from abc import ABC, abstractmethod
from enum import Enum
from random import choice
from typing import Optional


class Item(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    LIZARD = 4
    SPOK = 5

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
        if other is Item.SCISSORS or other is Item.LIZARD:
            return True
        elif other is Item.PAPER or other is Item.SPOK:
            return False
        elif other is Item.ROCK:
            raise Tie


class Paper(Strategy):
    item = Item.PAPER

    @staticmethod
    def check(other: Item) -> bool:
        if other is Item.ROCK or other is Item.SPOK:
            return True
        elif other is Item.SCISSORS or other is Item.LIZARD:
            return False
        elif other is Item.PAPER:
            raise Tie


class Scissors(Strategy):
    item = Item.SCISSORS

    @staticmethod
    def check(other: Item) -> bool:
        if other is Item.PAPER or other is Item.LIZARD:
            return True
        elif other is Item.ROCK or other is Item.SPOK:
            return False
        elif other is Item.SCISSORS:
            raise Tie


class Lizard(Strategy):
    item = Item.LIZARD

    @staticmethod
    def check(other: Item) -> bool:
        if other is Item.PAPER or other is Item.SPOK:
            return True
        elif other is Item.ROCK or other is Item.SCISSORS:
            return False
        elif other is Item.LIZARD:
            raise Tie


class Spok(Strategy):
    item = Item.SPOK

    @staticmethod
    def check(other: Item) -> bool:
        if other is Item.ROCK or other is Item.SCISSORS:
            return True
        elif other is Item.PAPER or other is Item.LIZARD:
            return False
        elif other is Item.SPOK:
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
        elif self.item is Item.LIZARD:
            return Lizard.check(other)
        elif self.item is Item.SPOK:
            return Spok.check(other)


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
        elif strategy is Item.LIZARD:
            self.strategy = Lizard()
        elif strategy is Item.SPOK:
            self.strategy = Spok()

    def play(player1, player2: 'Player') -> 'Player':
        if DEBUG:
            print(f'{player1.name} {player1.strategy.item.name}')
            print(f'{player2.name} {player2.strategy.item.name}')
        try:
            win = player1.strategy.check(player2.strategy.item)
            if DEBUG:
                print(f'Победил {(player2.name, player1.name)[win]}')
            return (player2, player1)[win]
        except Tie:
            if DEBUG:
                print('Ничья')
            player1.change_strategy()
            player2.change_strategy()
            return player1.play(player2)

    def __str__(self):
        return self.name


DEBUG = True

p1 = Player('Иван')
p2 = Player('Алла')
p3 = Player('Карл')

p1.play(p2).play(p3)
