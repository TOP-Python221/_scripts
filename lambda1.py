from pprint import pprint

def func(x):
    return x + 1

print(f"{func}\t{type(func)}")
# pprint(dir(func))
print()


f = lambda x: x + 1

print(f"{f}\t{type(f)}")
# pprint(dir(f))
print()


l = '0123456789'
l_f = ''.join(filter(lambda el: 3 <= int(el) < 6, l))

d = {'id1': {('p', 12398): (1+1j, 2+1j, 3+1j, 4+1j),
             ('q', 41137): (1+1j, 2+1j, 3+1j, 4+1j)},
     'id2': {('z', 94658): (3+7j, 6+7j, 9+8j, 12+7j),
             ('v', 88633): (3-6j, 6-6j, 9-6j, 12-5j)},
     'id3': {('z', 94658): (2+7j, 4+7j, 6+8j, 8+7j),
             ('v', 88633): (2+6j, 4+6j, 6+6j, 8+5j)},}

d_f = dict(filter(lambda pair: all(el.imag > 0 for iter in pair[1].values() for el in iter), d.items()))

d_f2 = {k: v for k, v in d.items() if all(el.imag > 0 for iter in v.values() for el in iter)}

def realkey(pair):
    q = sum(cnum.real for iter in pair[1].values() for cnum in iter)
    # print(q)
    return q

lambda pair: sum(cnum.real for iter in pair[1].values() for cnum in iter)

d_s = dict(sorted(d.items(), key=realkey))

for k, v in d_s.items():
    print(f"{k!r}\n{v!r}\n")
