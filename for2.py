n = int(input())

flag = False
for i in range(1, n+1):
    for j in range(1, (n+1)//2):
        print(f'{i = }\t{j = }')
        if (i*j) % 13 == 0:
            print(f'\t{i*j = }\n')
            flag = True
            break
    if flag:
        break
