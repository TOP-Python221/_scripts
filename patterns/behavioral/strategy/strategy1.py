class A:
    def __repr__(self):
        return 'машиночитаемое представление'

    def __str__(self):
        return 'человекочитаемое представление'

a = A()

print(repr(a))
print(str(a))

print(f'\n{a!r}')
print(f'{a!s}')
