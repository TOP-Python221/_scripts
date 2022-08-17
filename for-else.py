hex = '0123456789abcdef'

while s := input('number base 16: '):
    for c in s:
        if c not in hex:
            print(f'{s} is not hex\n')
            break
    # блок else выполняет только если цикл был завершён корректно –
    # без использования оператора break, и отработав все итерации
    else:
        print(f'{s} is hex\n')
