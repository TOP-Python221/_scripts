from random import randrange as rr, choice as ch
from pprint import pprint

# d3 = [rr(-10, 11) for _ in range(rr(5))]
# d2 = {rr(10, 20): rr(100, 200) for _ in range(rr(3))}
# d1 = {chr(rr(ord('a'), ord('z')+1)): ch((d2, d3)) for _ in range(rr(1, 5))}
# data = {rr(10): ch((d1, d3, rr(1000, 2000))) for _ in range(rr(2, 7))}
# подставляем выражения для d1, d2, d3 в те места, где они вызываются
data = {rr(10): ch(({chr(rr(ord('a'), ord('z')+1)): ch(({rr(10, 20): rr(100, 200) for _ in range(rr(3))}, [rr(-10, 11) for _ in range(rr(5))])) for _ in range(rr(1, 5))}, [rr(-10, 11) for _ in range(rr(5))], rr(1000, 2000))) for _ in range(rr(2, 7))}

pprint(data)
print()


def getkeysrecur(data: dict) -> set:
    """Recursive function to get all dict keys from all the way deep into tha data."""
    res = set()
    for k, v in data.items():
        if type(v) is dict:
            res |= getkeysrecur(v)
        res |= {k}
    return res

def getvaluesrecur(data) -> tuple:
    """Recursive function to get all dict values from all the way deep into tha data."""
    res = tuple()
    if type(data) is dict:
        for v in data.values():
            res += getvaluesrecur(v)
    elif isinstance(data, (list, tuple)):
        for el in data:
            res += getvaluesrecur(el)
    else:
        res += (data,)
    return res


print(getkeysrecur(data))
print(getvaluesrecur(data))
