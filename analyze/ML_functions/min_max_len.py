def ml_min(values):
    values = sorted(values)
    return values[0]

def ml_max(values):
    values = sorted(values, reverse=True)
    return values[0]

def ml_len(values):
    for i, _ in enumerate(values):
        pass
    return i+1