from random import randrange as rr

a = [rr(-9, 10) for _ in range(15)]
print(a, end='\n\n')

b = list(map(lambda x: abs(x), a))
print(b, end='\n\n')


d = {rr(10, 100): chr(rr(100, 200)) for _ in range(10)}
print(d, end='\n\n')

d_s1 = dict(sorted(d.items()))
print(d_s1, end='\n\n')

d_s2 = dict(sorted(d.items(), key=lambda x: x[1]))
print(d_s2, end='\n\n')
