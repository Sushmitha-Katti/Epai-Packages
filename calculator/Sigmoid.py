#Sigmoid.py
import math
__all__ = ['sigmoid']
def sigmoid(x):
    """
    returns sigmoid(x) for a given x
    """
    return 1/(1+math.exp(-x))