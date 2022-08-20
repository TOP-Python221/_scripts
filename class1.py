from pprint import pprint

class Table:
    legs = 4
    width = 100
    depth = 80
    height = 70

    def print(self):
        print(f'<{self.legs}-legs table: '
              f'{self.width}x{self.depth}x{self.height}>')


# создание экземпляров класса
table1 = Table()
table2 = Table()

print(f'{table1 = }\n{type(table1) = }\n')
print(f'{table2 = }\n{type(table2) = }\n')

print(f'{table1.legs = }')
print(f'{table1.height = }\n')

table1.legs = 4
table1.width = 100
table1.depth = 80
table1.height = 40

table2.legs = 3
table2.width = 50
table2.depth = 50
table2.height = 100

table3 = Table()

print(f'{table1.legs is Table.legs = }')
print(f'{table2.legs is Table.legs = }')
print(f'{table3.legs is Table.legs = }\n')

try:
    print('table1.print()')
    table1.print()
except TypeError as e:
    print('TypeError:', e)
    print('Вызов метода table1.print() становится вызовом функции Table.print(table1)\n')

table3.square = False
try:
    print('print(table2.square)')
    print(table2.square)
except AttributeError as e:
    print('AttributeError:', e, end='\n\n\n')


# вывод области видимости класса
print('dir(Table)')
pprint([name for name in dir(Table) if not name.startswith('__')])
# вывод пространства имён класса
print('Table.__dict__')
pprint(Table.__dict__)
print()

# вывод области видимости экземпляра
print('dir(table1)')
pprint([name for name in dir(table1) if not name.startswith('__')])
# вывод пространства имён экземпляра
print('table1.__dict__')
pprint(table1.__dict__)
print()

# вывод области видимости экземпляра
print('dir(table2)')
pprint([name for name in dir(table2) if not name.startswith('__')])
# вывод пространства имён экземпляра
print('table2.__dict__')
pprint(table2.__dict__)
print()

# вывод области видимости экземпляра
print('dir(table3)')
pprint([name for name in dir(table3) if not name.startswith('__')])
# вывод пространства имён экземпляра
print('table3.__dict__')
pprint(table3.__dict__)
print()


table1.print()  # Table.print(table1)
table2.print()  # Table.print(table2)
table3.print()  # Table.print(table3)
