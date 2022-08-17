import itertools as it

from functools import reduce
from operator import add

from string import ascii_letters as alt
from random import choice as ch, randrange as rr

iter1 = [''.join((ch(alt), ch(alt))) for _ in range(7)]
iter2 = list(range(1, 10))

print(f"{iter1 = }")
print(f"{iter2 = }\n")

print("reduce(lambda x, y: x+y, iter1)", end=' = ')
print(reduce(lambda x, y: x+y, iter1))
print("reduce(lambda x, y: x+y, iter2)", end=' = ')
print(reduce(add, iter2))

print("reduce(lambda x, y: x**y, iter2[1:5])", end=' = ')
print(reduce(lambda x, y: x**y, iter2[1:5]))
