from random import randrange as rr

def addmatrix(matrix1, matrix2, n=None, m=None):
    if not n: n = len(matrix1)
    if not m: m = len(matrix2)
    return tuple([tuple([matrix1[i][j]+matrix2[i][j] for j in range(m)]) 
                  for i in range(n)])

def printmatrix(matrix):
    mx_len = max([max([len(str(num)) for num in row]) for row in matrix]) + 1
    rows = [''.join([f'{num:>{mx_len}}' for num in row]) for row in matrix]
    print('\n', '\n'.join(rows), '\n', sep='')


n, m = map(int, input('matrix dimension: ').split())

matr1 = tuple([tuple([rr(1, 2000) for _ in range(m)]) 
               for _ in range(n)])
printmatrix(matr1)

matr2 = tuple([tuple([rr(1, 200) for _ in range(m)]) 
               for _ in range(n)])
printmatrix(matr2)

matr_sum = addmatrix(matr1, matr2, n, m)
printmatrix(matr_sum)
