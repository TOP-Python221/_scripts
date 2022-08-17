# 2**5 = 2 * 2**4 = 2 * 2 * 2**3 = ... = 2 * 2 * 2 * 2 * 2

def power(base: int, exp: int) -> int:
    """Recursive function for calc power of the number."""
    if exp == 1:
        print('начало возвратов')
        print(f'возврат функции power({base}, {exp}) -> {base}')
        return base
    else:
        print(f'вызов функции power({base}, {exp-1})')
        q = base * power(base, exp-1)
        print(f'возврат функции power({base}, {exp-1}) -> {q}')
        return q

b, e = int(input('base: ')), int(input('exp: '))
print(f'вызов функции power({b}, {e})')
print(power(b, e))
