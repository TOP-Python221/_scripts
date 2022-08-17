from random import randrange as rr

d = {(n := rr(-20, 21)): n**3 for _ in range(20)}

for i in range(-20, 21):
    print(f"{i = }\t{d.get(i, 0)}")
    d.setdefault(i, 0)
