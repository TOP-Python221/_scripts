def func(*, flag1, flag2, flag3, flag4):
    if flag1:
        print('First')
    if flag2:
        print('Second')
    if flag3:
        print('Third')
    if flag4:
        print('Fourth')

# приведёт к ошибке
# func(True, False, True, True)

func(flag1=True, flag2=False, flag3=False, flag4=True)
