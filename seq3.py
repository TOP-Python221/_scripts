# вывести пары рядом стоящих символов введённой строки

s = input('string: ')

for i in range(0, len(s), 2):
    print(f'{s[i:i+1]}{s[i+1:i+2]}! Парам-пам-пам!')
print()

for i in range(0, len(s), 2):
    print(f'{s[i]}', end='')
    if i+1 < len(s):
        print(f'{s[i+1]}', end='')
    print('! Парам-пам-пам!')
print()


if len(s) % 2 == 0:
    for i in range(0, len(s), 2):
        print(f'{s[i:i+1]}{s[i+1:i+2]}! Парам-пам-пам!')
else:
    # s = s[:-1]
    s += ' '
    for i in range(0, len(s), 2):
        print(f'{s[i:i+1]}{s[i+1:i+2]}! Парам-пам-пам!')
