from random import randrange as rr, choice as ch
from pprint import pprint

# d3 = [rr(-10, 11) for _ in range(rr(7))]
# d2 = ''.join(chr(rr(97, 123)) for _ in range(rr(8)))
# d1 = tuple(ch((rr(-10, 11), d2, d3)) for _ in range(rr(6)))
# data = [ch((d1, d2, d3)) for _ in range(rr(10))]
# подставляем выражения для d1, d2, d3 в те места, где они вызываются
data = [ch((tuple(ch((rr(-10, 11), ''.join(chr(rr(97, 123)) for _ in range(rr(8))), [rr(-10, 11) for _ in range(rr(7))])) for _ in range(rr(6))), ''.join(chr(rr(97, 123)) for _ in range(rr(8))), [rr(-10, 11) for _ in range(rr(7))])) for _ in range(rr(10))]

pprint(data)
print()


def flattening(iter) -> tuple:
    """Put all values from nested data structure to the flat tuple."""
    res = tuple()
    for elem in iter:
        if isinstance(elem, (list, tuple)):
            res += flattening(elem)
        else:
            res += (elem,)
    return res


print(flattening(data))
