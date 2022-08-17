from array import array

naturals = array('b', range(20))

for num in naturals:
    print(num, end=' ')
print('\n')

for i in range(len(naturals)-1):
    print(naturals[i:i+2].tolist(), end=' ')
print('\n')

# основная причина использовать массивы:
try:
    print("\nnaturals.append('s')")
    naturals.append('s')
except Exception as e:
    print(f"{e.__class__.__name__}: {e!s}")

try:
    print("\nnaturals.append(1.1)")
    naturals.append(1.1)
except Exception as e:
    print(f"{e.__class__.__name__}: {e!s}")

try:
    print("\nnaturals.append(1000)")
    naturals.append(1000)
except Exception as e:
    print(f"{e.__class__.__name__}: {e!s}")
