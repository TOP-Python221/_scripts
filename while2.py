while True:
    left = int(input('левая граница: '))
    right = int(input('правая граница: '))
    step = int(input('шаг: '))

    el = left
    while el < right if step > 0 else el > right:
        print(el, end=' ')
        el += step
    print()

    if input('выйти? ') == 'y':
        break
