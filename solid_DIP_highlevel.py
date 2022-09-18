import solid_DIP_lowlevel as model


class Research:
    def __init__(self, relations_base: model.Relationships):
        self.base = relations_base

    # нарушение принцип инверсии зависимостей: данный метод зависит от низкоуровневой реализации хранилища (итерируемое хранилище, кортежи, индексы)
    def find_all_children(self, name: str):
        for entry in self.base.storage:
            if entry[0].name.lower() == name.lower():
                if entry[1] is model.Relation.PARENT:
                    yield entry[2]


steve_research = Research(model.db)
for child in steve_research.find_all_children('steve'):
    print(child)
