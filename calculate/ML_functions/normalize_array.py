from .min_max_len import *
def normalize_array(array):
    data = list(array)
    mi = ml_min(data)
    ma = ml_max(data)
    for i, value in enumerate(data):
        data[i] = (value - mi) / (ma - mi)
    return data