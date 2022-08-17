(lambda: print('lambda'))()

# ТАК НЕ ДЕЛАЕМ
fl1 = lambda: print('saved lambda')

# то же самое
def fl2():
    print('saved lambda')
