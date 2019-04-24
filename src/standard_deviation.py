#!/usr/bin/python

import fileinput

from src.staff.math_api import *


def average(numbers):
    summary = 0
    for num in numbers:
        summary = add(summary, num)
    return divide(summary, len(numbers))


def N2x(numbers):
    return multiply(len(numbers), power(average(numbers), 2))


def big_sum(numbers):
    summary = 0
    nx2 = N2x(numbers)

    for num in numbers:
        summary = add(summary, sub(power(num, 2), nx2))

    return summary


def formula(numbers):
    return root(divide(abs(big_sum(numbers)), len(numbers) - 1), 2)


def main_fun():
    numbers = []

    for line in fileinput.input():
        if line == "\n":
            break
        numbers.append(Decimal(line))

    print(formula(numbers))


main_fun()
