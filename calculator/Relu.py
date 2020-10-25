#Relu.py
import math
__all__ = ['relu']
def relu(x):
    """
    returns relu(x) for a given x
    """
    return x if x >  0 else 0