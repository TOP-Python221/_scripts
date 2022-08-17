from collections import defaultdict as dd

d1 = dd(str)

d1[0.1] = '1'
d1[0.2] = '2'
d1[0.3] = d1[0.7] + '7'


d2 = dd(int)
d2[0.1] = 1
d2[0.2] = 2
d2[0.3] = d2[0.7] + 7
