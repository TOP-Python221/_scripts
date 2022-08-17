from random import randrange as rr

col1 = [rr(-200, 201) for _ in range(100)]
col2 = [''.join([chr(rr(97, 123)) for _ in range(rr(4, 8))]) 
        for _ in range(100)]
col3 = [rr(1, 20) for _ in range(100)]

  #  abcdj  | -183 |  3 
  # ————————————————————
  #  afv    |  45  | 12 
  # ————————————————————

rows = tuple()
for i in range(100):
    rows += ('|' + '|'.join( (' ' + col2[i].ljust(8), 
                              f'{col1[i]:^6}', 
                              f'{col3[i]:>3} ') ) + '|', )

print(('\n' + '—'*23 + '\n').join(('',) + rows + ('',)))
