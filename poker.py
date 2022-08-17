from random import randrange as rr

def checkhand(hand):
    check = set(hand)
    if len(check) > 1:
        if len(check) == 2:
            for card in check:
                if hand.count(card) == 4:
                    # каре – 4 одинаковые карты
                    # hand (2, 2, 2, 1, 2) -> check (2, 1)
                    return 'каре'
            else:
                # фулл хаус – 3 одинаковые карты и 2 другие одинаковые карты
                # hand (9, 3, 9, 3, 3) -> check (9, 3)
                return 'фулл хаус'
        # стрит – 5 последовательно идущих карт
        # hand (12, 9, 10, 8, 11) -> sorted (8, 9, 10, 11, 12)
        i = sorted(hand)[0]
        if sorted(hand) == list(range(i, i+5)):
            return 'стрит'
        if len(check) == 3:
            for card in check:
                # сет – 3 одинаковые карты
                # hand (11, 3, 6, 11, 11) -> check (11, 3, 6)
                if hand.count(card) == 3:
                    return 'сет'
            else:
                # две пары – 2 одинаковые карты и 2 другие одинаковые карты
                # hand (10, 10, 4, 8, 4) -> check (10, 4, 8)
                return 'две пары'
        # пара – 2 одинаковые карты
        # hand (12, 5, 3, 7, 12) -> check (12, 5, 3, 7)
        if len(check) == 4:
            return 'пара'
        return 'старшая карта'
    else:
        print('Шулер')

comb, turns = '', 0
while comb != 'каре':
    turns += 1
    hand = tuple([rr(1, 14) for _ in range(5)])
    comb = checkhand(hand)

print(hand, comb, turns, sep='\n')
