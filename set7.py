from random import randrange as rr

physics = [rr(2, 6) for _ in range(100)]
chemistry = [rr(2, 6) for _ in range(100)]
math = [rr(2, 6) for _ in range(100)]
biology = [rr(2, 6) for _ in range(100)]
russian = [rr(2, 6) for _ in range(100)]
informatics = [rr(2, 6) for _ in range(100)]

for i in range(100):
    score = {physics[i], chemistry[i], math[i], biology[i], russian[i], informatics[i]}
    if score == {5}:
        print(f'круглый отличник: {i}')
    if not (score & {2, 3}):
        print(f'нет двоек и троек: {i}')
    if not (score ^ {2, 3}):
        print(f'на отчисление: {i}')
