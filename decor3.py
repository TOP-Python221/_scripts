from typing import Callable


def decorator_generator(parameter) -> Callable:
    print(f'функция генератор декораторов принимает на вход параметр {parameter}')

    def decorator(func_object: Callable) -> Callable:
        print(f'\tфункция декоратор видит параметр декоратора {parameter}')

        def _wrapper(*args, **kwargs):
            print(f'\t\tфункция, подменяющая декорируемую функцию, тоже видит параметр декоратора {parameter}')
            res = func_object(*args, *kwargs)
            return res

        return _wrapper

    return decorator



def test():
    print('\t\t\tдекорируемая функция ни фига не видит, кроме своих персональных аргументов')

test = decorator_generator(2022)(test)
print(test)
test()


@decorator_generator('PARAMETER')
def adder(a, b):
    print('\t\t\tдекорируемая функция ни фига не видит, кроме своих персональных аргументов')
    return a + b

adder(4, 7)
