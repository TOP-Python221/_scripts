# функция вернёт None
def myfunc():
    print('print from without return')
    print('end of function without return\n')

# функция вернёт a
def myfunc2():
    print('print from function with return')
    a = 5
    print('end of function with return\n')
    return a

a = myfunc()
b = myfunc2()

print(a, b, end='\n\n')
