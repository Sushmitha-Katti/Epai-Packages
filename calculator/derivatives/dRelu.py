#Relu.py
import math
__all__ = ['relu']
def relu(x):
    """
    returns derative of relu(x)  which is 1 for x > 0 else 0
    """
    return 1 if x >  0 else 0