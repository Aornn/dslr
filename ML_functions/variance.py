from .min_max_len import *
from .mean import *
def variance(array):
    n = ml_len(array)
    m = mean(array)
    res = 1/(n-1)*(sum((x - m)**2 for x in array))
    return res