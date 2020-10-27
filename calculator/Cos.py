#Cos.py
import math
from calculator.utils import print_f

__all__ = ['cos']

@print_f
def cos(x:float) -> float :
    """
    returns cos(x) for a given x
    x should be in radians
    """
    return math.cos(x)


@print_f
def dcos(x :float) -> float:
    """
    returns derivative of cos(x) which is -sin(x)
    """
    return -math.sin(x)