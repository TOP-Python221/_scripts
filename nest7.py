from random import randrange as rr

n, m = map(int, input('matrix dimension: ').split())

matr1 = tuple([tuple([rr(1, 20) for _ in range(m)]) 
               for _ in range(n)])
matr2 = tuple([tuple([rr(1, 20) for _ in range(m)]) 
               for _ in range(n)])

matr_sum = tuple([tuple([matr1[i][j] + matr2[i][j] 
                         for j in range(m)]) 
                  for i in range(n)])

rows = [''.join([f'{num:>3}' for num in row]) for row in matr1]
print('\n'.join(rows), end='\n\n')

print('\n'.join([''.join([f'{num:>3}' for num in row]) 
                 for row in matr2]), end='\n\n')

print('\n'.join([''.join([f'{num:>3}' for num in row]) 
                 for row in matr_sum]), end='\n\n')
