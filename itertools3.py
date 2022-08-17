from datetime import datetime as dt
import itertools as it
from string import ascii_letters as alt
from random import choice, randrange as rr

iter1 = [''.join((choice(alt), choice(alt), choice(alt))) for _ in range(5)]
iter2 = tuple(rr(100, 1000) for _ in range(7))

print(f"{iter1 = }")
print(f"{iter2 = }\n")

print("zip(iter1, iter2)")
for pair in zip(iter1, iter2):
    print(pair)
print()

print("it.zip_longest(iter1, iter2, fillvalue='')")
for pair in it.zip_longest(iter1, iter2, fillvalue=''):
    print(pair)
print()
