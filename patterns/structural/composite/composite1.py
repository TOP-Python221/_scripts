from abc import ABC, abstractmethod
from dataclasses import dataclass


class VectorGraphic(ABC):
    @abstractmethod
    def render(self):
        pass


@dataclass
class Line(VectorGraphic):
    name: str
    length: int

    def render(self):
        print(f'{self.name}: {self.length}')


@dataclass
class Text(VectorGraphic):
    name: str
    text: str

    def render(self):
        print(f'{self.text}')


class GroupElements(VectorGraphic):
    def __init__(self, name: str):
        self.name = name
        self.elements: list[VectorGraphic] = []

    def add_elements(self, element: VectorGraphic, *elements: VectorGraphic):
        elements = (element, ) + elements
        self.elements = list(elements)

    def render(self):
        for elem in self.elements:
            elem.render()


ab = Line('AB', 2)
bc = Line('BC', 5)
cd = Line('CD', 2)
da = Line('DA', 5)
formula = Text('perimeter', 'P = AB + BC + CD + DA')

ab.render()
da.render()
formula.render()

print()

figure = GroupElements('Rectangle Perimeter')
figure.add_elements(ab, bc, formula, cd, da)

figure.render()
