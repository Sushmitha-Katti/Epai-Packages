import math
import numpy as np

__all__ = ['dsoftmax']
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

    