from fractions import Fraction as F
from math import e

n1 = F(1, 2)
n2 = F(2, 3)

n3 = n1 + n2
n4 = n2 - n1

print(f"{n3 = !r}\t{n3.numerator = }\t{n3.denominator = }")
print(f"{n4 = !r}\t{n4.numerator = }\t{n4.denominator = }\n")

n5 = F('12/25')
n6 = F('-0.224')
n7 = F(0.8)

print(f"{n5 = !s}\t{n5.numerator = }\t{n5.denominator = }")
print(f"{n6 = !s}\t{n6.numerator = }\t{n6.denominator = }")
print(f"{n7 = !s}\t{n7.numerator = }\t{n7.denominator = }\n")

e_close = F(e).limit_denominator(1000)

print(f"{e_close = }\t{e_close.__round__(5) = }")
