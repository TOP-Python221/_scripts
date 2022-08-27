from math import sqrt
from fractions import Fraction as F


class Tetrahedron:
    def __init__(self, edge: float):
        self.edge = edge

    @property
    def edge(self) -> float:
        return self._edge

    @edge.setter
    def edge(self, new_edge: float) -> None:
        self._edge = new_edge
        self._surface = new_edge**2 * sqrt(3)
        self._volume = new_edge**3 * sqrt(2) / 12

    @property
    def surface(self) -> float:
        return self._surface

    @surface.setter
    def surface(self, new_surface: float) -> None:
        self._edge = sqrt(new_surface/sqrt(3))
        self._surface = new_surface
        self._volume = self._edge**3 * sqrt(2) / 12

    @property
    def volume(self) -> float:
        return self._volume

    @volume.setter
    def volume(self, new_volume: float) -> None:
        self._edge = (new_volume*12/sqrt(2))**F(1, 3)
        self._surface = self._edge**2 * sqrt(3)
        self._volume = new_volume


th1 = Tetrahedron(5)
th1_scope = [name for name in dir(th1) if not name.startswith('__')]
print(f'\n{th1_scope = }')

print(f"\n{th1.__dict__ = }")
th1.volume = 100
print(f"\n{th1.__dict__ = }")
