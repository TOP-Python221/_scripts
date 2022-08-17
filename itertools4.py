from datetime import datetime as dt
import itertools as it
from string import ascii_letters as alt
from random import choice, randrange as rr

iter1 = 'ABC'
iter2 = list(range(1, 5))

print(f"{iter1 = }")
print(f"{iter2 = }\n")

print(f"it.permutations(iter1) = {tuple(it.permutations(iter1))}")
print(f"it.permutations(iter1) = {tuple(it.permutations(iter2))}\n")

print(f"it.combinations(iter1, 2) = {tuple(it.combinations(iter1, 2))}")
print(f"it.combinations(iter1, 2) = {tuple(it.combinations(iter2, 2))}\n")



