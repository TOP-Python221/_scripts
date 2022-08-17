l = input().split()
for el in l:
    print(el)

for i in range(len(l)):
    if l[i].isdecimal() or \
       l[i][0] == '-' and l[i][1:].isdecimal():
        l[i] = int(l[i])
