#Sin.py
import math
__all__ = ['dsin']
def dsin(x:float) ->float:
    """
    returns derivative of sin(x) which is  cos(x)
    """
    return math.cos(x)