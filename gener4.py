from random import randrange as rr

# генераторное выражение
g = (rr(-10, 11) for _ in range(20))
print(type(g), end='\n\n')

for n in g:
    print(n, end=' ')
print()



gl1 = [rr(-10, 11) for _ in range(20)]
# при передаче генераторного выражения в качестве аргумента 
#   дополнительные круглые скобки не требуются
gl2 = list(rr(-10, 11) for _ in range(20))

print(f'{sum(rr(-10, 11) for _ in range(20)) = }')


print(*(rr(-10, 11) for _ in range(20)))
