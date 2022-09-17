"""Opened-Closed Principle — Принцип Открытости/Закрытости"""
from abc import ABC, abstractmethod
from typing import Iterable


class Goods:
    """Информация о товаре."""
    def __init__(self, name: str, color: str, size: str):
        self.name = name
        self.color = color
        self.size = size


class GoodsFilter:
    """Фильтрация некоторого количества товаров по разным критериям."""
    def __init__(self, goods: Iterable):
        self.goods = goods

    def filter_by_color(self, color: str):
        """Генератор возвращает товары, чей цвет соответствует переданному аргументу."""
        for g in self.goods:
            if g.size == color:
                yield g

    def filter_by_size(self, size: str):
        """Генератор возвращает товары, чей размер соответствует переданному аргументу."""
        for g in self.goods:
            if g.size == size:
                yield g

    def filter_by_color_and_size(self, color: str, size: str):
        """Генератор возвращает товары, чьи и размер и цвет соответствуют переданным аргументам."""
        for g in self.goods:
            if g.size == color and g.size == size:
                yield g

    # нарушение принципа открытости/закрытости
    # взрывной рост количества требуемых для фильтрации методов при увеличении количества критериев

    # 2 критерия: a, b
    # комбинации: a, b, ab

    # 3 критерия: a, b, c
    # комбинации: a, b, c, ab, bc, ac, abc

    # 4 критерия: a, b, c, d
    # комбинации: a, b, c, d, ab, bc, cd, ac, bd, ad, abc, abd, bcd, acd, abcd



# реализация без нарушения принципа открытости/закрытости

class Criteria(ABC):
    """Абстрактный базовый класс для различных критериев фильтрации."""
    @abstractmethod
    def is_satisfied(self, product: Goods):
        """Проверяет, соответствует ли определённый параметр продукта определённому критерию."""
        pass


class Color(Criteria):
    """Критерий цвета."""
    def __init__(self, color: str):
        self.color = color.lower()

    def is_satisfied(self, product: Goods):
        """Проверяет, соответствует ли цвет продукта данному критерию цвета."""
        return self.color == product.color.lower()


class Size(Criteria):
    """Критерий размера."""
    def __init__(self, size: str):
        self.size = size.lower()

    def is_satisfied(self, product: Goods):
        """Проверяет, соответствует ли размер продукта данному критерию размера."""
        return self.size == product.size.lower()


class AndCrit(Criteria):
    """Логическое умножение на объединение критериев."""
    def __init__(self, *criteria: Criteria):
        self.criteria = criteria

    def is_satisfied(self, product: Goods):
        """Проверяет, соответствуют ли параметры продукта каждому из перечисленных в объединении критериев."""
        return all(map(
            lambda crit: crit.is_satisfied(product),
            self.criteria
        ))


class Filter(ABC):
    """Абстрактный базовый класс для реализации различных логик фильтрации."""
    @abstractmethod
    def filter(self, criteria: Criteria):
        pass


class CritFilter(Filter):
    """Реализация фильтра с хранением объектов товаров в поле экземпляра."""
    def __init__(self, goods: Iterable):
        self.goods = goods

    def filter(self, criteria: Criteria):
        """Генератор возвращает товары, которые удовлетворяют объекту критерия."""
        for pr in self.goods:
            if criteria.is_satisfied(pr):
                yield pr



catalog = [
    Goods('Брюки', 'чёрный', 'средний'),
    Goods('Рубашка', 'белый', 'средний'),
    Goods('Рубашка', 'жёлтый', 'большой'),
    Goods('Куртка', 'коричневый', 'малый'),
    Goods('Шапка', 'чёрный', 'большой'),
]

simple_stupid_filter = GoodsFilter(catalog)

# print('\nЧёрные вещи:')
# filtered = simple_stupid_filter.filter_by_color('чёрный')
# for i, pr in enumerate(filtered):
#     print(f'{i+1}. {pr.name}')
#
# print('\nБольшие вещи:')
# filtered = simple_stupid_filter.filter_by_size('большой')
# for i, pr in enumerate(filtered):
#     print(f'{i+1}. {pr.name}')
#
# print('\nСредние белые вещи:')
# filtered = simple_stupid_filter.filter_by_color_and_size('белый', 'средний')
# for i, pr in enumerate(filtered):
#     print(f'{i+1}. {pr.name}')


smart_filter = CritFilter(catalog)

black = Color('чёрный')
print(f'\nЦвет {black.color}:')
filtered = smart_filter.filter(black)
for i, pr in enumerate(filtered):
    print(f'{i+1}. {pr.name}')

small = Size('малый')
print(f'\nРазмер {small.size}:')
filtered = smart_filter.filter(small)
for i, pr in enumerate(filtered):
    print(f'{i+1}. {pr.name}')

yellow = Color('жёлтый')
large = Size('большой')
yellow_large = AndCrit(yellow, large)
print(f'\nЦвет {yellow.color}, Размер {large.size}:')
filtered = smart_filter.filter(yellow_large)
for i, pr in enumerate(filtered):
    print(f'{i+1}. {pr.name}')
