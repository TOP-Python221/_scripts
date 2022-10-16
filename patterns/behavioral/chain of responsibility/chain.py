from typing import Optional


class Creature:
    """Обрабатываемый объект."""
    def __init__(self,
                 name: str,
                 default_attack: int,
                 default_defense: int):
        self.name = name.title()
        self.attack = default_attack
        self.defense = default_defense

    def __str__(self):
        return f'{self.name}: A={self.attack}, D={self.defense}'


class CreatureModifier:
    """Базовый класс для цепочки обработчиков. Запускает обработку данных."""
    def __init__(self, creature: Creature):
        # обрабатываемый объект
        self.creature = creature
        # поля для связи с другими обработчиками в цепочке
        self.previous_modifier: Optional['CreatureModifier'] = None
        self.next_modifier: Optional['CreatureModifier'] = None

    def add_modifier(self, modifier: 'CreatureModifier'):
        """Добавляет обработчик."""
        if self.next_modifier is None:
            self.next_modifier = modifier
        else:
            self.next_modifier.add_modifier(modifier)

    def handle(self):
        """Вызывает следующий обработчик в цепочке."""
        if self.next_modifier is not None:
            self.next_modifier.handle()


class DoubleAttackModifier(CreatureModifier):
    """Обработчик атаки."""
    def handle(self):
        """Модифицирует атрибуты обрабатываемого объекта."""
        self.creature.attack *= 2
        super().handle()


class IncreaseDefenseModifier(CreatureModifier):
    """Обработчик защиты."""
    def handle(self):
        """Модифицирует атрибуты обрабатываемого объекта."""
        if self.creature.attack <= 2*self.creature.defense:
            self.creature.defense += 1
        super().handle()


goblin = Creature('Гоблин', 1, 1)
print(goblin)

inventory = CreatureModifier(goblin)

wood_club = DoubleAttackModifier(goblin)
inventory.add_modifier(wood_club)

inventory.handle()
print(goblin)

# clothes = IncreaseDefenseModifier(goblin)
# inventory.add_modifier(clothes)
