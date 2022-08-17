n = int(input('matrix rows: '))
# заполнение матрицы из ввода с помощью представления списка
matr = [[int(num) for num in input().split()] for _ in range(n)]

matr2 = [[num**2 for num in row] for row in matr]
