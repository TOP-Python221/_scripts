print('start')
a = '1'
try:
    a += 1
    print(f'{a = }')
except NameError:
    print('проблема с именами')
except TypeError:
    print('проблема с типами')
except:
    print('что-то пошло не так...')

print('end')
