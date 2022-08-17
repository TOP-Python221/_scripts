l = [[1, 2, 3, 4], 
     [5, 6, 7, 8], 
     [9, 10, 11, 12], 
     [13, 14, 15, 16]]

l2 = [[1, 2, 3, 4], 
      [5, 6, 7, 8], 
      [9, 10, 11, 12], 
      [13, 14, 15, 16]]

for i in range(len(l)):
    for j in range(len(l[i])):
        print(f'{i = }\t{j = }\t{l[i][j] = }')
        l[i][j] = i*j
    print()

for row in l2:
    for el in row:
        print(f'{el = }')
        el = 34
    print()
