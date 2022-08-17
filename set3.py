from random import randrange as rr

# возвращают новое множество
alphabet = {chr(i) for i in range(1072, 1104)}.union({'ё'})
alphabet = {chr(i) for i in range(1072, 1104)} | {'ё'}
# изменяют существующее множество
alphabet.update({'ё'})
alphabet |= {'ё'}

set_from_text = set(input().lower())

sub = set_from_text.issubset(alphabet)
sub = set_from_text <= alphabet
sup = set_from_text.issuperset(alphabet)
sup = set_from_text >= alphabet
dis = set_from_text.isdisjoint(alphabet)
print(f'\nset_from_text подмножество alphabet: {sub}')
print(f'set_from_text надмножество alphabet: {sup}')
print(f'set_from_text не пересекается с alphabet: {dis}')

set_intersect = set_from_text & alphabet
print(f'\nПересечение set_from_text и alphabet: {set_intersect}')

set_diff1 = set_from_text - alphabet
set_diff2 = alphabet - set_from_text
print(f'\nРазность set_from_text и alphabet: {set_diff1}')
print(f'Разность alphabet и set_from_text: {set_diff2}')

set_symdiff = set_from_text ^ alphabet
print(f'\nСимметричная разность set_from_text и alphabet: {set_symdiff}')
