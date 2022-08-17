# написать функцию, генерирующую пароль
# функция принимает на вход набор параметров, определяющих сложность пароля
# функция возвращает строку с паролем

from string import ascii_lowercase as alc, \
                   ascii_uppercase as auc, \
                   digits, punctuation
from random import choice

def generatepassword(maxlen: int = 8, *, 
                     lowercase: bool = True, 
                     uppercase: bool = False, 
                     digit: bool = True, 
                     puncs: bool = False) -> str:
    """Generate password using various characters sets."""
    all_chars = (('', alc)[lowercase]
                 + ('', auc)[uppercase]
                 + ('', digits)[digit]
                 + ('', punctuation)[puncs])
    # print(all_chars)
    return ''.join(choice(all_chars) for _ in range(maxlen))

def checkpassword(password: str) -> str:
    """Check if passed string is weak or strong password."""
    def calcpercent(criterias: tuple) -> str:
        """"""
        p = sum(map(int, criterias)) / len(criterias)
        if p <= 0.2:
            return 'very weak'
        elif 0.2 < p < 0.5:
            return 'weak'
        elif p == 0.5:
            return 'normal'
        elif 0.5 < p < 0.8:
            return 'strong'
        elif p >= 0.8:
            return 'very strong'
    res = (len(password) > 5, 
           password.lower() != password, 
           password.isnumeric(), 
           bool(set(punctuation) & set(password)))
    return calcpercent(res)



p1 = generatepassword()
p2 = generatepassword(12)
p3 = generatepassword(uppercase=True)
p4 = generatepassword(uppercase=True, digit=False)

a = [generatepassword(3, digit=False) for _ in range(12)]
