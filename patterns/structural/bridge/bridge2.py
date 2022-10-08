from abc import ABC, abstractmethod


class Material(ABC):
    @abstractmethod
    def __str__(self):
        pass

class Straw(Material):
    def __str__(self):
        return 'straw'

class Wood(Material):
    def __str__(self):
        return 'wooden'

class Cobblestone(Material):
    def __str__(self):
        return 'cobblestone'

class Brick(Material):
    def __str__(self):
        return 'brick'


class Building(ABC):
    def __init__(self, material: Material):
        self.material = material

    @abstractmethod
    def __str__(self):
        pass


class Watchtower(Building):
    def __init__(self, name: str, material: Material):
        super().__init__(material)
        self.name = name

    def __str__(self):
        return f'{self.material} watchtower {self.name}'


class Mill(Building):
    def __init__(self, name: str, material: Material):
        super().__init__(material)
        self.name = name

    def __str__(self):
        return f'{self.material} mill {self.name}'


wt1 = Watchtower('The Long Shadow Tower of West Edge', Wood())
print(wt1)

wt2 = Watchtower('East Coast First Aid Watchtower', Straw())
print(wt2)
