from .min_max_len import *
from .mean import *

def variance(array):
    n = ml_len(array)
    m = mean(array)
    res = (sum((x - m)**2 for x in array))/n
    return res