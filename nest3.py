matr = []
n = int(input('matrix rows: '))

# заполнение матрицы из ввода
for i in range(n):
    matr += [input().split()]
print()

# поиск максимального
mx = 0
# лобовой
# for row in matr:
    # for el in row:
        # if mx < len(el): 
            # mx = len(el)

# с использованием функции max() – более быстрый
for row in matr:
    q = len(max(row, key=len))
    if mx < q:
        mx = q

# вывод выровненной матрицы
for row in matr:
    for num in row:
        print(f'{num:_>{mx}s}', end=' ')
    print()
