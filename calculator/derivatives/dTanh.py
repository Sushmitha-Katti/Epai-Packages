#Tanhx
import math
__all__ = ['dtanh']
def dtanh(x:float)->float : 
    """
    returns derivative of tanh(x) which is 1 - x^2
    """
    return 1 - x**2