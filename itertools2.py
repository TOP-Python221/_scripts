from datetime import datetime as dt
import itertools as it
from string import ascii_letters as alt
from random import choice, randrange as rr

iter1 = [''.join((choice(alt), choice(alt), choice(alt))) for _ in range(5)]
iter2 = tuple(rr(100, 1000) for _ in range(5))

print(f"{iter1 = }")
print(f"{iter2 = }\n")

for elem in it.chain(iter1, iter2):
    print(elem, end=' ')
print('\n')

select1 = [choice((True, False)) for _ in range(5)]
print(f"{select1 = }")

print(f"compress(iter2, select1) = {list(it.compress(iter2, select1))}\n")

print(f"filter(lambda x: x.islower(), iter1) = {list(filter(lambda x: x.islower(), iter1))}")

def predicate1(element):
    return True if element < 500 else False

def myfilter(func_predicate, iter):
    for elem in iter:
        if func_predicate(elem):
            yield elem

print(f"filter(predicate1, iter2) = {list(myfilter(predicate1, iter2))}\n")

print(f"it.filterfalse(lambda x: x.islower(), iter1) = {list(it.filterfalse(lambda x: x.islower(), iter1))}")
print(f"it.filterfalse(predicate1, iter2) = {list(it.filterfalse(predicate1, iter2))}\n")


