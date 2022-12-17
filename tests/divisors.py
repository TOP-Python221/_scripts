__all__ = [
    'get_divisors',
]

def get_divisors(number: int) -> list[int]:
    result = []
    for div in range(abs(number)//2 + 1, 0, -1):
        if number % div == 0:
            result += [number]
    return result


# arrange
zero = 0
prime = 1
positive = 44
negative = -12

# add
def test_divisors_zero():
    # assert
    assert get_divisors(zero) == []

# add
def test_divisors_prime():
    # assert
    assert len(get_divisors(prime)) == 2

# add
def test_divisors_positive():
    # assert
    assert len(get_divisors(positive)) >= 2

# add
def test_divisors_negative():
    # assert
    assert len(get_divisors(negative)) >= 2

