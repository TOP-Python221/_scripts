# на вход функции подаётся список из строк с математическими операторами
# функция возвращает список с кортежами, содержащими те же строки 
#   и числа – приоритеты соответствующих операторов
#   где меньшее число соответствует более высокому приоритету

# вход функции:
#   ['*', '+', '/', '^']
# выход функции:
#   [('*', 2), ('+', 3), ('/', 2), ('^', 1)]

def precedence(*operators):
    return [(oper, 1 if oper == '^' else (2 if oper in '*/' else 3)) 
            for oper in operators]

# 2 * 3 + 4 / 2 ^ 2
m_str = input('math string: ')
m_opers = [elem for elem in m_str.split() if not elem.isdecimal()]

print(precedence(*m_opers), end='\n\n')

print(precedence('+', '-'))
