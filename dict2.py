d = {1: 'a', 
     2.5: [1, 2, 3], 
     'key': 123, 
     ('el1', 'el2'): {1: 'a', 2: 'b'}}

print('\nkey in d')
for key in d:
    print(f"{key = }  {d[key] = }")

print('\nkey in d.keys()')
for key in d.keys():
    print(f"{key = }  {d[key] = }")

print('\nvalue in d.values()')
for value in d.values():
    print(f"{value = }")

print('\npair in d.items()')
for pair in d.items():
    print(f"{pair}")

print('\nk, v in d.items()')
for k, v in d.items():
    print(f"{k = }  {v = }")
