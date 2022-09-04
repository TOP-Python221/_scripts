
class IntExtra(int):
    # def __new__(cls, value: int):
    #     return int.__new__(cls, value)

    def is_prime(self):
        for d in range(2, self//2 + 1):
            if self % d == 0:
                return False
        else:
            return True

    def __add__(self, other):
        res = super().__add__(other)
        return IntExtra(res)

    def __radd__(self, other):
        res = super().__radd__(other)
        return IntExtra(res)

    def __floordiv__(self, other):
        res = super().__floordiv__(other)
        if isinstance(res, int):
            return IntExtra(res)
        else:
            return res


n1 = 5
n2 = IntExtra(7)

print(f"{n1 = }\t{type(n1) = }")
print(f"{n2 = }\t{type(n2) = }\n")

print(f"{n1.__class__.__mro__ = }")
print(f"{n2.__class__.__mro__ = }\n")

print(f"{n2.is_prime() = }\n")

n3 = n1 + n2
n4 = n2 + n2
print(f"{n3 = }\t{type(n3) = }")
print(f"{n4 = }\t{type(n4) = }\n")

n5 = n4 // 2
n6 = n4 // 2.5
print(f"{n5 = }\t{type(n5) = }")
print(f"{n6 = }\t{type(n6) = }\n")




