from datetime import datetime as dt
import itertools as it
from string import ascii_letters as alt
from random import choice, randrange as rr

for i in it.count(0, 100):
    if i > 10**6:
        break
    print(i)

start = dt.today()
for elem in it.cycle(['abc', 23, 3.98]):
    if (dt.today() - start).seconds > 3:
        break
    print(elem, end=' ')
print()
