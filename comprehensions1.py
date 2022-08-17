from random import randrange as rr

l1 = [i*10 for i in range(1, 10)]

l2 = [i for i in range(90, 110) if i**2 % 10 in (4, 6)]

l3 = [l2[rr(4):rr(3,7)] for _ in range(5)]

l4 = [elem for list_ in l3 for elem in list_]

l5 = [int(''.join(sorted([ch for ch in str(elem) if ch != '1']))) 
      for list_ in l3 for elem in list_]
