from .mean import *
from .min_max_len import *
def std (values):
    m = mean(values)
    res = sum(abs(x - m)**2 for x in values)
    return (res/(ml_len(values)))**0.5