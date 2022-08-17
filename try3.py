# LBYL (LBL) — Look Before You Leap — Смотри Куда Прёшь
def sort_LBYL(iter):
    """Sorts while keeping argument's type"""
    if type(iter) is list:
        iter.sort()
        return iter
    elif type(iter) is tuple:
        return tuple(sorted(iter))

# EAFP (AFP) — Easier Ask Forgivness than Permisson — Проси Прощения, не Разрешения
def sort_EAFP(iter):
    """Sorts while keeping argument's type"""
    try:
        iter.sort()
    except:
        iter = tuple(sorted(iter))
    finally:
        return iter


l = [3, 2, 4, 1]
t = (1, 4, 2, 3)

print(sort_EAFP(l))
print(sort_EAFP(t))
