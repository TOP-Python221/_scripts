from pprint import pprint

def f1():
    print(a)
    print('locals from f1')
    pprint(locals())
    print()

def f2():
    a = b*2
    print(a)
    print('locals from f2')
    pprint(locals())
    print()

def f3():
    # а - локальная переменная, 
    #   потому что в функции есть соответствующая инструкция присваивания
    # обращение к ней до объявления вызовет ошибку
    print(a)
    a = b*3
    print('locals from f3')
    pprint(locals())
    print()

a, b = 0, 'z'

f1()
f2()
f3()

print('globals from top level')
pprint(globals())
print()
