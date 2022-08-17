l = []
while s := input():
    l += [s]

for c in ' \t,:':
    print('\n' + c.join(l))
