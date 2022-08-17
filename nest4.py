matr = []
n = int(input('matrix rows: '))

# заполнение матрицы из ввода с помощью представления списка
matr = [input().split() for _ in range(n)]
print()

# поиск максимального с использованием функций max() и представления списка
mx = max([len(max(row, key=len)) for row in matr])


# вывод выровненной матрицы
_ = [print(' '.join([f'{num:_>{mx}s}' for num in row]))
     for row in matr]
