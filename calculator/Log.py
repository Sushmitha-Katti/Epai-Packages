#Log.py
import math
__all__ = ['log']
def log(x:float) -> float:
    """
    returns log(x) for a given x
    """
    return math.log(x)



def dlog(x:float) -> float:
    """
    returns derivative of log(x) which is 1/x
    """
    return 1/x