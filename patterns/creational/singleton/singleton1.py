"""Демонстратор одиночки: реализация с использованием атрибута класса."""


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            return cls._instance
        else:
            return cls._instance


class Test:
    pass


test1 = Test()
test2 = Test()
print(f'{test1 is test2 = }')

inst1 = Singleton()
inst2 = Singleton()
print(f'{inst1 is inst2 = }')

Singleton._instance = None
inst3 = Singleton()
print(f'{inst2 is inst3 = }')
