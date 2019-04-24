import math
from decimal import Decimal


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def absolute(a):
    return abs(a)


def divide(a, b):
    if b == 0:
        return 'nan'
    else:
        return a / b


def multiply(a, b):
    return a * b


def factorial(a):
    return math.factorial(a)


def power(a, b):
    return math.pow(Decimal(a), Decimal(b))


def root(a, b):
    return math.pow(Decimal(a), Decimal(1.0) / b)
