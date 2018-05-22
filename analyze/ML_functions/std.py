from .mean import *
from .min_max_len import *
def std (values):
    m = mean(values)
    res = sum((x - m)**2 for x in values)
    return (res/(ml_len(values)-1))**0.5