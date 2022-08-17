def f1(n, m):
    for i in range(n):
        for j in range(m):
            if i*j == 10:
                return j
a = f1(4, 6)
print(a)



flag = False
for i in range(4):
    for j in range(6):
        if i*j == 10:
            flag = True
            break
    if flag:
        break
print(a)
a = j
