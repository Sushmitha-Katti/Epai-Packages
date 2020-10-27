
  
from functools import wraps

__all__ = ['print_f']

def print_f(fn: "Function"):
    """
    Decorator that lets a function run and prints whatever is returned.
    """
    @wraps(fn)
    def inner(*args, **kwargs):
        output = fn(*args, **kwargs)
        print(f'Output of {fn.__name__}: {output}')
        return output
    return inner