from pprint import pprint
from import2 import *

print(f'\n{IM2 = }')

pprint(globals())

print(f'\n{import1.IM1 = }')

IM2 = 250
print(f"\n{IM2 = }\t{get_IM2() = }")

import1.IM1 = 150
print(f"\n{import1.IM1 = }\t{import1.get_IM1() = }")
