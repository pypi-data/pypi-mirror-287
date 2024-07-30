from .param import param
from .phi import PHI


def weight(key, shape):
    return param(key, shape) + PHI
