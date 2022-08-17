from random import randrange as rr

alphabet = {chr(i) for i in range(1072, 1104)}
set_from_text = set(input().lower())

flag = set_from_text.issubset(alphabet)
print(f'Подмножество: {flag}')
flag = set_from_text.issuperset(alphabet)
print(f'Надмножество: {flag}')
