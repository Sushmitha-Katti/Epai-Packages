#Sin.py
import math
from calculator.utils import print_f

__all__ = ['sin']
@print_f
def sin(x: float) -> float :
    """
    returns sin(x) for a given x
    x should be in radians
    """
    return math.sin(x)

@print_f
def dsin(x:float) ->float:
    """
    returns derivative of sin(x) which is  cos(x)
    """
    return math.cos(x)