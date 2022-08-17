from random import randrange as rr

def addmatrix(matrix1, matrix2, *matrices, n=None, m=None):
    matrices = (matrix1, matrix2) + matrices
    if n is None:
        n = len(matrices[0])
    if m is None:
        m = len(matrices[0][0])
    return tuple([tuple([sum(matr[i][j] for matr in matrices)
                         for j in range(m)]) 
                  for i in range(n)])

def printmatrix(matrix):
    mx_len = max([max([len(str(num)) for num in row]) for row in matrix]) + 1
    rows = [''.join([f'{num:>{mx_len}}' for num in row]) for row in matrix]
    print('\n', '\n'.join(rows), '\n', sep='')

LIM = 10

n, m = map(int, input('matrix dimension: ').split())

matr1 = tuple([tuple([rr(1, LIM) for _ in range(m)]) 
               for _ in range(n)])
printmatrix(matr1)

matr2 = tuple([tuple([rr(1, LIM) for _ in range(m)]) 
               for _ in range(n)])
printmatrix(matr2)

matr3 = tuple([tuple([rr(1, LIM) for _ in range(m)]) 
               for _ in range(n)])
printmatrix(matr3)


print('matrix sum: ')
# приведёт к ошибке
# matr_sum = addmatrix(matr1)

# размерность матриц вычисляется функцией
matr_sum = addmatrix(matr1, matr3)
printmatrix(matr_sum)

# передача размерности в строго ключевые параметры
matr_sum = addmatrix(matr1, matr2, matr3, n=n, m=m)
printmatrix(matr_sum)
