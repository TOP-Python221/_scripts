def simple_decor(function_object):
    def _wrapper():
        print('Decorator starts working')
        function_object()
        print('Decorator ends working')
    return _wrapper

def func():
    print('Function is working')


print(f"{func.__name__}", 
      f"{type(func) = }", 
      f"{id(func) = }", 
      sep='\n', end='\n\n')

decorator = simple_decor(func)

print(f"{decorator.__name__}", 
      f"{type(decorator) = }", 
      f"{id(decorator) = }", 
      sep='\n', end='\n\n')

func = simple_decor(func)

print(f"{func.__name__}", 
      f"{type(func) = }", 
      f"{id(func) = }", 
      sep='\n', end='\n\n')


@simple_decor
def func2():
    print('Function 2 is working')

