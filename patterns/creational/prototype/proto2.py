"""Демонстратор прототипа: реализация для отдельного класса."""

from dataclasses import dataclass, field
from copy import deepcopy


@dataclass
class BlueprintDoc:
    name: str
    paper_number: str
    pieces: int = 1
    paper_format: str = 'A4'
    standards_set: list[str] = field(default_factory=list)
    # ...

    def clone(self) -> 'BlueprintDoc':
        return deepcopy(self)


item1_paper = BlueprintDoc(
    'Изделие 1',
    'СПВ-КУ.121-01',
    1,
    'А3',
    ['ГОСТ 1477-93', 'ГОСТ 10618-80', 'ГОСТ 10619-80']
)

item2_paper = item1_paper.clone()
item2_paper.name = 'Изделие 2'
item2_paper.paper_number = 'СПВ-КР.122-01'
