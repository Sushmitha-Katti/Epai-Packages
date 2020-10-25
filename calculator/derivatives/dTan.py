#Tan.py
import math
__all__ = ['dtan']
def dtan(x):
    """
    returns derivative of tan(x) which is sec(x)^2 == 1/cos(x)^2
    """
    return 1/(math.cos(x)**2)