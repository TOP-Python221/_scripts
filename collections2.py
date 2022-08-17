from collections import namedtuple as nt

Point = nt('Point', ['x', 'y'])
p1 = Point(0, 2)
p2 = Point(x=3, y=-1)

table = []
with open('collections2.csv') as fh_in:
    Table = nt('Table', fh_in.readline().rstrip().split(','))
    for line in fh_in.readlines():
        table += [Table(*line.rstrip().split(','))]
