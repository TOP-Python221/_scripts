def func1():
    return 'call from'

def func2():
    return 'call from'

def func3():
    return 'call from'

def func4():
    return 'call from'


fs = (func1, func2, func3, func4, )

for func in fs:
    print(func(), func.__name__)
