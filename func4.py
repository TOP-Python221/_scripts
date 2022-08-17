def add(number1=0, number2=0):
    print(locals())
    # print(f'{id(number1) = }')
    if (isinstance(number1, (int, float)) 
        and isinstance(number2, (int, float))):
        return number1 + number2
    elif type(number1) is str and type(number2) is str:
        if number1.isdecimal() and number2.isdecimal():
            return int(number1) + int(number2)

a = 15978654
# print(f'{id(a) = }')

print(add(a, 4.5), end='\n\n')

print(add(100), end='\n\n')

print(add('15', '12'), end='\n\n')

print(add(), end='\n\n')
