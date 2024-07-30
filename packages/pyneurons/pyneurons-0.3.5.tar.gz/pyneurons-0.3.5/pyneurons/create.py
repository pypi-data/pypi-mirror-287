from .weight import weight
from .bias import bias


def create(key, n):
    w = weight(key, shape=(n, 1))
    b = bias(key, shape=(1, 1))
    return (w, b)
