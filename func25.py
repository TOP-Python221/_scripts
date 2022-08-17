# n1 = 16    n2 = 12
# 16 % 12 = 4
# 12 % 4 = 0
# 4

def gcd(number1: int, number2: int) -> int:
    """Recurcive function to calc greatest common divider."""
    if number2 == 0:
        print('начало возвратов')
        print(f'возврат функции gcd({number1}, {number2}) -> {number1}')
        return number1
    else:
        print(f'вызов функции gcd({number2}, {number1 % number2})')
        q = gcd(number2, number1 % number2)
        print(f'возврат функции gcd({number2}, {number1 % number2}) -> {q}')
        return q

while True:
    a = input('n1: ')
    if not a:
        break
    else:
        a = int(a)
    b = int(input('n2: '))
    print(f'вызов функции gcd({a}, {b})')
    print(gcd(a, b), end='\n\n')
