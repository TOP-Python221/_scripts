from functools import lru_cache
from random import randrange as rr

@lru_cache(maxsize=2)
def testfunc(a, b):
    return rr(a, b)
