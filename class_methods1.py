from random import randrange as rr, choice, sample

CAT_COLORS = ['black', 'white', 'sand', 'grey', 'brown', 'orange']

class Cat:
    def __init__(self,
                 name: str,
                 sex: str,
                 weight: float,
                 colors: list[str]):
        self.name = name
        self.sex = sex
        self.weight = weight
        self.colors = colors

    def __str__(self):
        return f'<{self.name.title()}: {self.sex}, {"-".join(self.colors)}>'

    # для статических методов:
    # instance.method(*args) -> Class.method(*args)
    @staticmethod
    def meow() -> None:
        print('Meow!')

    # для обычных методов:
    # instance.method(*args) -> Class.method(instance, *args)
    def ask_for_food(self) -> None:
        for _ in range(rr(3, 6)):
            self.meow()

    def reproduce(self) -> 'Cat':
        if self.sex == 'F':
            return Cat('<name>',
                       choice('MF'),
                       0.05,
                       sample(CAT_COLORS, k=rr(1, 4)))


cat1 = Cat('Яра', 'F', 3.64, ['grey', 'white', 'black'])
print(cat1)

cat1.meow()
print()

cat1.ask_for_food()
print()

cat2 = cat1.reproduce()
print(cat2)
