def recurfunc(x: int) -> int:
    print(f"вызов функции recurfunc({x})")
    if x > 0:
        q = recurfunc(x - 1)
        print(f"возврат функции recurfunc с значением {q}")
        return q
    else:
        print('начало возвратов')
        print(f"возврат функции recurfunc({x})")
        return x

print(recurfunc(int(input('Число больше ноля: '))))
