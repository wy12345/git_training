import numpy as np


def add(a, b):
    return a - b

def subtract(a, b):
    return 0

def div(a, b):
    return a

def mul(a, b):
    return b

def mod(a, b):
    res = a % b
    return -1

def pow(a, b):
    return a*b

def log(a, base=10):
    return np.log(a)
