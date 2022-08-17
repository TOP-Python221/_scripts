def gen2(num):
    q = num
    print('generator start', end=' ')
    while num < 10:
        yield num
        num += 1
    num = -q
    while num > -10:
        yield num
        num -= 1
    print('generator stop')

def gen3(num):
    while num < 10:
        yield num
        yield -num
        num += 1


for n in gen2(5):
    print(n, end=' ')
print()

a = gen3(5)
b = list(a)
print(b)
