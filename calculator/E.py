import math
__all__ = ['e']
def e(x:float) -> float:
    """
    calculates e^x for a given x
    """
    return math.exp(x)



def de(x:float)->float:
    """
    returns derivative of e^x which is e^x
    """
    return math.exp(x)