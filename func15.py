def func(**kwargs):
    print(type(kwargs))
    print(kwargs)

func(a=1, b=2, c='z')

# приведёт к ошибке
func(True, a=1, b=2, c='z')
