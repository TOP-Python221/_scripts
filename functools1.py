from functools import partial
from decimal import Decimal as D

def hxy(*args, **kwargs):
    """Полиномиальная функция одной или двух переменных с n = m = 2."""
    x = args[0] if len(args) > 0 else 0
    y = args[1] if len(args) > 1 else 0
    n = kwargs.get('n', 1)
    m = kwargs.get('m', 1)
    a = kwargs.get('a', 1)
    return x**n - y**m + a*(y - x)

hxy2 = partial(hxy, n=2 , m=2)
hxy3 = partial(hxy, n=3 , m=3)
