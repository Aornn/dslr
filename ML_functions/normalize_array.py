from .min_max_len import *
def normalize_array(array):
    mi = ml_min(array)
    ma = ml_max(array)
    for i, value in enumerate(array):
        array[i] = (value - mi) / (ma - mi)
    return array