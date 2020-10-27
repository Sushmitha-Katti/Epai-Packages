#Relu.py
import math
from calculator.utils import print_f

__all__ = ['relu']
@print_f
def relu(x:float) -> float:
    """
    returns relu(x) for a given x
    """
    return x if x >  0 else 0

@print_f
def drelu(x: int) -> int:
    """
    returns derative of relu(x)  which is 1 for x > 0 else 0
    """
    return 1 if x >  0 else 0