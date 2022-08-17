def gen_inf(num, step=1):
    while True:
        yield num
        num += step

LIM = 10**6
for n in gen_inf(0, 100):
    if n > LIM:
        break
    print(n)
