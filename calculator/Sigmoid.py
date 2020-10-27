#Sigmoid.py
from calculator.utils import print_f
import math
__all__ = ['sigmoid']
@print_f
def sigmoid(x:float) -> float:
    """
    returns sigmoid(x) for a given x
    """
    return 1/(1+math.exp(-x))

@print_f
def dsigmoid(x :float) ->float:
    """
    returns derivative  sigmoid(x) for a given x which is x(1-x)
    """
    return x *(1-x)