from functools import wraps

def debug_decor(function_object):
    @wraps(function_object)
    def _wrapper(*args, **kwargs):
        print(f'<debug> {function_object.__name__}')
        for arg in args:
            print(f'<debug>  {arg}, {type(arg)}')
        for k, v in kwargs.items():
            print(f'<debug>  {k}={v}, {type(v)}')
        ret = function_object(*args, **kwargs)
        print(f'<debug> -> {ret}, {type(ret)}')
        return ret
    return _wrapper


@debug_decor
def sq_polynom(x: float, 
               a: float = 1, 
               b: float = 0, 
               c: float = 0) -> float:
    """Calculates square polynom: ax\u00b2 + bx + c"""
    return round(a*x**2 + b*x + c, 1)


@debug_decor
def cu_polynom(x: float, 
               a: float = 1, 
               b: float = 0, 
               c: float = 0,
               d: float = 0) -> float:
    """Calculates cube polynom: ax\u00b3 + bx\u00b2 + cx + d"""
    return round(a*x**3 + b*x**2 + c*x + d, 1)


@debug_decor
def gcd(number1: int, number2: int) -> int:
    """Recurcive function to calc greatest common divider."""
    if number2 == 0:
        return number1
    else:
        return gcd(number2, number1 % number2)


# print(sq_polynom(2), end='\n\n')
# print(cu_polynom(2, d=2), end='\n\n')

# print(gcd(100, 30))

