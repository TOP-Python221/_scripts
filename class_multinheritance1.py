class Mother:
    eyes = 'blue'
    def care(self):
        print('care')

class Father:
    hair = 'black'
    def fight(self):
        print('fight')


class Child(Mother, Father):
    pass


children = (
    Child(),
    Child()
)

print(f'{children[0].eyes =}')
print(f'{children[0].hair =}\n')
print(f'{children[1].eyes =}')
print(f'{children[1].hair =}\n')
