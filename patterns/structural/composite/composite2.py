
class Neuron:
    def __init__(self, name: str):
        self.name = name
        self.inputs: list[Neuron] = []
        self.outputs: list[Neuron] = []

    def connect_to(self, other: 'Neuron'):
        self.outputs.append(other)
        other.inputs.append(self)

    def __iter__(self):
        yield self

    def __repr__(self):
        return (str(self)
                + '\n\tВходы:\n'
                + '\n'.join(f'\t{n!s}' for n in self.inputs)
                + '\n\tВыходы:\n'
                + '\n'.join(f'\t{n!s}' for n in self.outputs))

    def __str__(self):
        return f'{self.name}'


class NeuronLayer(list):
    def __init__(self, name: str, count: int):
        super().__init__()
        self.name = name
        for i in range(1, count+1):
            self.append(Neuron(f'Нейрон_слоя_{i}'))

    def connect_to(self, other):
        for neuron_out in self:
            for neuron_in in other:
                neuron_out.outputs.append(neuron_in)
                neuron_in.inputs.append(neuron_out)

    def __str__(self):
        return f'{self.name}\n' \
               + '\n'.join(f'\t{n!s}' for n in self)


n1 = Neuron('Отдельный_нейрон_1')
n2 = Neuron('Отдельный_нейрон_2')

n1.connect_to(n2)

print(f'{n1!r}\n')
print(f'{n2!r}\n')

nl1 = NeuronLayer('Слой_1', 2)
nl2 = NeuronLayer('Слой_2', 3)
print(nl1, end='\n\n')
print(nl2, end='\n\n')

nl1.connect_to(nl2)

nl1.connect_to(n1)
print(f'{n1!r}\n')
