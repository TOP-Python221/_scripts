def mymap(func, iter):
    res = tuple()
    for el in iter:
        res += (func(el),)
    return res


def fx(x):
    return x**2 - 4*x + 3

def gxy(x, y):
    return x**2 - y**2 + 5*(y - x)

def hxy(*args):
    x = args[0] if len(args) > 0 else 0
    y = args[1] if len(args) > 1 else 0
    return x**2 - y**2 + 5*(y - x)


x1_axis = tuple(range(-7, 8))
y1_axis = mymap(fx, x1_axis)

x2_axis = tuple(range(1, 32, 2))
y2_axis = mymap(lambda x: round((5 + 3*x)/x**2, 5), x2_axis)
