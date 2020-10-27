#Relu.py
import math
__all__ = ['drelu']
def drelu(x: int) -> int:
    """
    returns derative of relu(x)  which is 1 for x > 0 else 0
    """
    return 1 if x >  0 else 0