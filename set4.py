set1 = {1, 2, 3}
try:
    set1.add({4, 5})
except TypeError:
    print('объект set не может являться элементом объекта set')

fset1 = frozenset((4, 5))
set1.add(fset1)
print('объект frozenset может являться элементом объекта set')

set1.remove(1)
try:
    set1.remove(4)
except KeyError:
    print('в метод remove() нельзя передавать элементы, отсутствующие в множестве')

set1.discard(2)
set1.discard(4)
print('в метод discard() можно передавать элементы, отсутствующие в множестве')

print(set1.pop())
set1.add('last')
print(set1.pop())
