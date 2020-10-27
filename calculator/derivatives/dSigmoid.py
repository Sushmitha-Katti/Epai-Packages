#Sigmoid.py
import math
__all__ = ['dsigmoid']
def dsigmoid(x :float) ->float:
    """
    returns derivative  sigmoid(x) for a given x which is x(1-x)
    """
    return x *(1-x)