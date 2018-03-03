#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from lp_utils import separator


"""
This fill will cover the built in functions in Python. Focusing on Python 3.
Documentation can be found here:
https://docs.python.org/3/library/functions.html#abs
"""


separator("Absolute Value - Integer")
for number in range(-3, 4):
    abs_number = abs(number)
    print("abs({}) = {}".format(number, abs_number))

separator("Absolute Value - Floating Point")
for _ in range(6):
    # Generate a random float with a random sign
    float_ = random.random() * 5 * random.randint(-100, 100)
    abs_float = abs(float_)
    print("abs({}) = {}".format(float_, abs_float))

separator("Absolute Value - Complex Numbers - Returns the absolute value of the magnitude of the complex number.")
for _ in range(6):
    # Generate a random complex number with a random sign
    complex_ = complex(0, random.random() * 5 * random.randint(-100, 100))
    abs_complex = abs(complex_)
    print("abs({}) = {}".format(complex_, abs_complex))


