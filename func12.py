def func(arg1, /, arg2, arg3, *, arg4):
    print(f"positional-only: {arg1}")
    print(f"positional-or-keyword: {arg2} {arg3}")
    print(f"keyword-only: {arg4}")

# приведёт к ошибке: последний аргумент строго ключевой
func(1, 2, 3, 4)

func(1, 2, 3, arg4=4)
func(1, 2, arg3=3, arg4=4)
func(1, arg4=2, arg3=4, arg2=3)

# приведёт к ошибке: первый аргумент строго позиционный
func(arg1=1, arg4=2, arg3=4, arg2=3)
