#Tanh
import math
from calculator.utils import print_f
__all__ = ['tanh']

@print_f
def tanh(x:float) -> float : 
    """
    returns tanh(x) for a given x
    x should be in radians
    """
    return math.tanh(x)

@print_f
def dtanh(x:float)->float : 
    """
    returns derivative of tanh(x) which is 1 - x^2
    """
    return 1 - x**2