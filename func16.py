def func(arg1, *args, kwarg1, **kwargs):
    print(type(args), type(kwargs))
    print(args)
    print(kwargs)


t = tuple(range(-3, 4))
d = {f'{i}': chr(i) for i in range(200, 206)}

func(True, *t, kwarg1=True, **d)

# приведёт к ошибке
func(True, *t, True, **d)
