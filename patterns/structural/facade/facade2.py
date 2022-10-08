from dataclasses import dataclass
from random import choice, shuffle


@dataclass
class Hawk:
    name: str = 'H'
    alive: bool = True
    reproducing: bool = False

    def __str__(self):
        return self.name

    @staticmethod
    def move():
        return 'attack'

    @staticmethod
    def reproduce():
        return Hawk()


@dataclass
class Dove:
    name: str = 'D'
    alive: bool = True
    reproducing: bool = False

    def __str__(self):
        return self.name

    @staticmethod
    def move():
        return 'defense'

    @staticmethod
    def reproduce():
        return Dove()


def iterate(population: list[Hawk, Dove]) -> list[Hawk, Dove]:
    half = len(population) // 2
    part_left = population[:half]
    part_right = population[half:]

    for a1, a2 in zip(part_left, part_right):
        move1, move2 = a1.move(), a2.move()

        if move1 == 'attack':
            if move2 == 'attack':
                # два ястреба
                a1.alive = False
                a2.alive = False
            elif move2 == 'defense':
                # ястреб и голубь
                a1.reproducing = True
                a2.alive = False
        elif move1 == 'defense':
            if move2 == 'defense':
                # голубь и ястреб
                a1.alive = False
                a2.reproducing = True
            elif move2 == 'defense':
                # два голубя
                choice((a1, a2)).reproducing = True

    species = []
    for animal in part_left + part_right:
        if animal.alive:
            species += [animal]
            if animal.reproducing:
                species += [animal.reproduce()]
    return species



class Simulation:
    def __init__(self, hawks: int, doves: int):
        self.population = []
        for _ in range(hawks):
            self.population.append(Hawk())
        for _ in range(doves):
            self.population.append(Dove())
        shuffle(self.population)

    def show_animals(self):
        print(' '.join(str(animal) for animal in self.population))

    def iterate(self) -> bool:
        self.population = iterate(self.population)
        shuffle(self.population)
        return bool(self.population)



s1 = Simulation(4, 20)
s1.show_animals()

while s1.iterate():
    s1.show_animals()
