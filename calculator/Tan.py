#Tan.py
from calculator.utils import print_f
import math
__all__ = ['tan']

@print_f
def tan(x:float)->float:
    """
    returns tan(x) for a given x
    x should be in radians
    """
    return math.tan(x)
@print_f
def dtan(x:float)->float:
    """
    returns derivative of tan(x) which is sec(x)^2 == 1/cos(x)^2
    """
    return 1/(math.cos(x)**2)