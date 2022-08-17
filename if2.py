print('='*10, 'КВАДРАТНОЕ УРАВНЕНИЕ', '='*10, 
	 '\n\nax\u00b2 + bx + c = 0')

while True:
    while (a := int(input('\na = '))) == 0:
        print('в квадратном уравнении коэффициент а не может быть равен нулю')

    b, c = int(input('b = ')), int(input('c = '))

    equ = f'\n{("-" if a == -1 else a) if a != 1 else ""}x\u00b2 ' + \
          (f"- {abs(b)}x " if b < 0 else f"+ {b}x " if b > 0 else "") + \
          (f"- {abs(c)} " if c < 0 else f"+ {c} " if c > 0 else "") + '= 0'
    print(equ)

    D = b**2 - 4*a*c

    if D < 0:
        print('\nнет вещественных корней у уравнения')
    elif D == 0:
        print(f'\nx = {-b / (2*a)}')
    else:
        print(f'\nx1 = {-b + D**-0.5 / (2*a):.3f}\n'
             f'x2 = {-b - D**-0.5 / (2*a):.3f}')

    if input('\nхотите решить ещё одно уравнение? ') != 'y':
        break
