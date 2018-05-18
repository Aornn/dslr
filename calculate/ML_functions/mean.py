from .min_max_len import *
def mean(values):
    total = 0
    l = ml_len(values)
    for value in values:
        total = float(total) + float(value)
    return float(total / l)