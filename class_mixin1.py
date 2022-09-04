class PrimeMethod:
    """Класс-примесь к базовому классу int."""
    def is_prime(self: int) -> bool:
        for d in range(2, self//2 + 1):
            if self % d == 0:
                return False
        else:
            return True


class IntWithPrimeIndication(int, PrimeMethod):
    pass


n1 = IntWithPrimeIndication(5)
print(f"\n{n1 = }\n{type(n1) = }")
print(f"\n{n1.__class__.__mro__ = }")
print(f"\n{n1 + 10 = }")
print(f"{type(n1 + 10) = }")
print(f"\n{n1.is_prime() = }\n")
