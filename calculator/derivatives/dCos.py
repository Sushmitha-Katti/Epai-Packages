#Cos.py
import math
__all__ = ['dcos']
def dcos(x):
    """
    returns derivative of cos(x) which is -sin(x)
    """
    return -math.sin(x)