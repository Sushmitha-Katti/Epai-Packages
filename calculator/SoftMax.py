import math
__all__ = ['softmax']
def softmax(x : list) -> list:
    """
    calculates softmax for a given list
    """
    if(isinstance(x,list)):
        e_x = [math.exp(i - max(x))  for i in x]
        return [i/sum(e_x) for i in e_x]
    else : 
        raise ValueError(f"Input must be a list")