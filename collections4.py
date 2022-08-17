from random import randrange as rr
from collections import ChainMap

d1 = {str(i): rr(10, 100) for i in range(1, 5)}
d2 = {str(i): rr(-100, -10) for i in range(-1, -5, -1)}

cm = ChainMap(d1, d2)

print(f"{cm['1'] = }\t{cm['-1'] = }\n")


d1['5'] = 55
print(f"{cm['5'] = }")
