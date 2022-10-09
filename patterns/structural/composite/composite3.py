class Connectable:
    """Класс-примесь для подключения нейронов и слоёв друг к другу."""
    def connect_to(self, other):
        if not self or not other:
            return

        for neuron_out in self:
            for neuron_in in other:
                neuron_out.outputs.append(neuron_in)
                neuron_in.inputs.append(neuron_out)


class Neuron(Connectable):
    def __init__(self, name: str):
        self.name = name
        self.inputs: list[Neuron] = []
        self.outputs: list[Neuron] = []

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


class NeuronLayer(list, Connectable):
    """Группа нейронов."""
    def __init__(self, name: str, count: int):
        super().__init__()
        self.name = name
        for i in range(1, count+1):
            self.append(Neuron(f'{self.name}_нейрон_{i}'))

    def __str__(self):
        return f'{self.name}\n' \
               + '\n'.join(f'\t{n!s}' for n in self)


n1 = Neuron('Отдельный_нейрон_1')
n2 = Neuron('Отдельный_нейрон_2')
nl1 = NeuronLayer('Слой_1', 2)
nl2 = NeuronLayer('Слой_2', 3)

nl1.connect_to(n1)
n1.connect_to(n2)
n2.connect_to(nl2)

for n in nl1:
    print(repr(n))
print(repr(n1))
print(repr(n2))
for n in nl2:
    print(repr(n))
