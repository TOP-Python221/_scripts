from decor2 import debug_decor

@debug_decor
def power_recur(base, exp):
    if exp == 1:
        return base
    else:
        return base * power_recur(base, exp - 1)

# print(power_recur(int(input('base: ')), int(input('exp: '))))


@debug_decor
def flat(nested_data: list | tuple) -> tuple:
    res = ()
    for el in nested_data:
        if isinstance(el, (list, tuple)):
            res += flat(el)
        else:
            res += (el,)
    return res

data = [1, 2, 3, 4, [5, [6, 7, ((8, 9), (10, 11)), 12, 13], 14], [15, 16, [17]]]
print(f"\n{flat(data)!s}\n")
