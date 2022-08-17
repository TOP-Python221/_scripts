
d = {1: 'a', 2.5: 'b', 'key': 123, ('el1', 'el2'): 9}

print(type(d))

print(d[1], d[2.5], d['key'], sep='\n')

d['1'] = 1
d['key'] = 'value'

s1 = ['e', 'l', '1']
s2 = ['e', 'l', '2']

print(d[(''.join(s1), ''.join(s2))])
