import math
from calculator.utils import print_f
import numpy as np
__all__ = ['softmax']

@print_f
def softmax(x : list) -> list:
    """
    calculates softmax for a given list
    """
    if(isinstance(x,list)):
        e_x = [math.exp(i - max(x))  for i in x]
        return [i/sum(e_x) for i in e_x]
    else : 
        raise ValueError(f"Input must be a list")

@print_f
def dsoftmax(x:list)->'np.ndarray':
    """
    This gives the derivative of softmax for a given array
    """
    #Reshape the 1-d softmax to 2-d so that np.dot will dp that matix multiplication
    if(isinstance(x,list)):
        x = np.array([x])
        s = x.reshape(-1,1)
        dsoft = np.diagflat(s) - np.dot(s, s.T)
        return dsoft
    else:
        raise ValueError(f"input must be a list")
