#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lp_utilities.random_gen import random_signed_integer, random_signed_float, random_signed_complex
from lp_utilities.separator import separator

"""
The abs() function returns the the Mathematical absolute value of the input value if
it can be understood as an integer, float, or complex number.

Complex numbers are numbers that contain imaginary components sqrt(-1)
For more information about complex numbers in python see:
* Complex - http://python-reference.readthedocs.io/en/latest/docs/functions/complex.html
"""

NUMBER_OF_TESTS_TO_RUN = 6


def print_abs(input_value, output_value):
    """
    This method just does formatting for the abs function examples
    :param input_value:   Number  The value sent to the abs() function
    :param output_value:  Number  The value the abs() function returns
    :return: Void
    """
    print("abs({}) = {}".format(input_value, output_value))


def abs_integer():
    separator("abs(integer) - Absolute Value - Integer")
    for _ in range(NUMBER_OF_TESTS_TO_RUN):
        integer_ = random_signed_integer(100)
        result = abs(integer_)
        print_abs(integer_, result)


def abs_float():
    separator("abs(float) - Absolute Value - Floating Point")
    for _ in range(NUMBER_OF_TESTS_TO_RUN):
        # Generate a random float with a random sign
        float_ = random_signed_float(100)
        result = abs(float_)
        print_abs(float_, result)


def abs_complex():
    separator("abs(complex) - Absolute Value - Complex Numbers - Returns the absolute value of the magnitude of the "
              "complex number.")
    for _ in range(NUMBER_OF_TESTS_TO_RUN):
        # Generate a random complex number with a random sign
        complex_ = random_signed_complex(100)
        result = abs(complex_)
        print_abs(complex_, result)


def abs_string():
    separator("abs(string) - Absolute Value - String")
    try:
        print_abs("5", abs("5"))
    except TypeError as e:
        print("Attempted to execute abs(\"{}\") and it throws a TypeError.".format(5))
        print("Strings cannot be passed to the abs function even if the contents of the string are numbers.")
        print("The exception message is:")
        print(e)


def main():
    abs_integer()
    abs_float()
    abs_complex()
    abs_string()


if __name__ == "__main__":
    # execute only if run as a script
    main()
