from .min_max_len import *
import numpy as np
def quartile(values):
    values = sorted(values)
    q1 = float(ml_len(values)) / 4.0
    q2 = q1 * 3.0
    ret1, ret2 = 0, 0
    if q1.is_integer():
        ret1 = values[int(q1)-1]
    if q2.is_integer():
        ret2 = values[int(q2)-1]
    if not ret1:
        full, deci = str(q1).split('.')
        ret1 = values[int(full)]
    if not ret2:
        full, deci = str(q2).split('.')
        ret2 = values[int(full)]
    return ret1, ret2


def mediane(values):
    values = sorted(values)
    med = (float(ml_len(values)) / 2) - 1
    if ml_len(values) % 2 == 0:
        return (values[int(med)] + values[int(med)+1]) / 2
    else:
        full, deci = str(med).split('.')
        return values[int(full) + 1]