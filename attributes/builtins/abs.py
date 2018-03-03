#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from lp_utilities.separator import separator

"""
The abs() function returns the the Mathematical absolute value of the input value if
it can be understood as an integer, float, or complex number.

Complex numbers are numbers that contain imaginary components sqrt(-1)
For more information about complex numbers in python see:
* Complex - http://python-reference.readthedocs.io/en/latest/docs/functions/complex.html
"""


def print_abs(input_value, output_value):
    print("abs({}) = {}".format(input_value, output_value))


separator("abs(integer) - Absolute Value - Integer")
for integer_ in range(-3, 4):
    result = abs(integer_)
    print_abs(integer_, result)


separator("abs(float) - Absolute Value - Floating Point")
for _ in range(6):
    # Generate a random float with a random sign
    float_ = random.random() * 5 * random.randint(-100, 100)
    result = abs(float_)
    print_abs(float_, result)


separator("abs(complex) - Absolute Value - Complex Numbers - Returns the absolute value of the magnitude of the "
          "complex number.")
for _ in range(6):
    # Generate a random complex number with a random sign
    complex_ = complex(0, random.random() * 5 * random.randint(-100, 100))
    result = abs(complex_)
    print_abs(complex_, result)
