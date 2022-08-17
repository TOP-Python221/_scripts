from pprint import pprint

import import1
import import2

print()
module_global = {name: obj 
                 for name, obj in globals().items()
                 if not name.startswith('__')}
pprint(module_global)

import1.IM1 = 125
import2.import1.IM1 = 150
# не ведёт к кольцевому импорту, т.к. модули import1 и import2 не являются выполняемыми
print(f"\n{import1.IM1 = }")
print(f"\n{import2.import1.IM1 = }")
