class Mother:
    eyes = 'blue'
    hair = 'brown'

class Father:
    eyes = 'green'
    hair = 'black'


class Child1(Mother, Father):
    pass

girl = Child1()
print(f'\n{girl.__class__.__mro__ = }\n')
print(f'{girl.eyes = }')
print(f'{girl.hair = }\n')
print(f'{girl.eyes = }')
print(f'{girl.hair = }\n')


class Child2(Father, Mother):
    pass

boy = Child2()
print(f'\n{boy.__class__.__mro__ = }\n')
print(f'{boy.eyes = }')
print(f'{boy.hair = }\n')
print(f'{boy.eyes = }')
print(f'{boy.hair = }\n')
