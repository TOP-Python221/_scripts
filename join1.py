s = ['abc', 'xyz', 'опр']

j1 = ''.join(s)
j2 = ' # '.join(s)
j3 = '\n'.join(s)

print(f"{j1 = !s}\n")
print(f"{j2 = !s}\n")
print(f"{j3 = !s}\n")


def myjoin(sep, iter):
    res = ''
    for elem in iter:
        if type(elem) is str:
            res += elem + sep
        else:
            raise ValueError
    return res[:-len(sep)] if sep else res

mj1 = myjoin('', s)
mj2 = myjoin(' # ', s)
mj3 = myjoin('\n', s)

print(f"{mj1 = !s}\n")
print(f"{mj2 = !s}\n")
print(f"{mj3 = !s}\n")
