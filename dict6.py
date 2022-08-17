cyr_alphabet = {chr(i+1071): i for i in range(1, 7)}\
                | {'ё': 7}\
                | {chr(i+1070): i for i in range(8, 34)}

cyr_alphabet_invert = {v: k for k, v in cyr_alphabet.items()}

d = {chr(i+1071): i for i in range(1, 7)}
d.update({'ё': 7})
d.update({chr(i+1070): i for i in range(8, 34)})
