"""Dependencies Inversion Principle — Принцип Инверсии Зависимостей"""

import solid_DIP_lowlevel as model


class Research:
    def __init__(self, relations_base: model.Relationships):
        self.base = relations_base

    def find_all_children(self, name: str):
        return self.base.find_all_children(name)


steve_research = Research(model.db)
for child in steve_research.find_all_children('steve'):
    print(child)
