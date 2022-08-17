def point(x, y, z, /, planar=True, flag=0):
    pass


point(0.5, 0.5, -0.5, flag=10, planar=False)

# приведёт к ошибке
point(planar=False, flag=0, x=0.5, y=0.5, z=-0.5)
