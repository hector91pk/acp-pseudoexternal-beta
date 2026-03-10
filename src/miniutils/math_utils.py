def add(a, b):
    return a + b


def clamp(value, min_v, max_v):
    return max(min_v, min(value, max_v))


def safe_div(a, b):
    if b == 0:
        return None
    return a / b