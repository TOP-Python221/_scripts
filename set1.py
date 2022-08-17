from random import randrange as rr

set1 = {1, 2, 3, 1}

set2 = {rr(10) for _ in range(50)}

l1 = [rr(10) for _ in range(50)]
set3 = set(l1)

s1 = 'строка с текстом для анализа'
set4 = set(s1)
