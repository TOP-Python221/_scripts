def cat(*args, sep=''):
    if not args:
        return None
    for arg in args:
        if type(arg) is not str:
            return None
    return sep.join(args)

print(cat())
print(cat('123'))
print(cat('123', 'abc'))
print(cat(123, 'abc'))
print(cat('1', '2', '3', 'a', 'b', 'c'))
print(cat('1', '2', '3', 'a', 'b', 'c', sep=' '))
