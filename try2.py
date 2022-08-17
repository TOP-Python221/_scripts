
try:
    a, b = int(input('num 1: ')), int(input('num 2: '))

except:
    print('что-то пошло не так')

else:
    print('успешный ввод')

finally:
    print('выполняется всегда')

