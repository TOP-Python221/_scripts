s = input('string: ')

for i in range(len(s)):
    print(i, end='\t')
print()

for c in s:
    print(c, end='\t')
print()

for i in range(-len(s), 0):
    print(i, end='\t')
print()
