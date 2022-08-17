from decimal import Decimal as D
from math import e

print("round(0.1, 1) + round(0.1, 1) + round(0.1, 1) == round(0.3, 1)")
print(round(0.1, 1) + round(0.1, 1) + round(0.1, 1) == round(0.3, 1), end='\n\n')

n1 = D(1)
n2 = D(10)

n3 = n1 / n2

print(f"{n3 = }\t{n3 = !s}\n")

print("round(D('0.1'), 1) + round(D('0.1'), 1) + round(D('0.1'), 1) == round(D('0.3'), 1)")
print(round(n3, 1) + round(n3, 1) + round(n3, 1) == round(D('0.3'), 1))


