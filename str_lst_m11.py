s = input('phrase: ')

if s.lower().startswith('hi'):
    print('Hi', end='')
    if s.endswith('!'):
        print('!')
    else:
        print('.')
else:
    print('Nothing to see here...')
