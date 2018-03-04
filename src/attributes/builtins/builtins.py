#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from decimal import Decimal
from fractions import Fraction
from lp_utils import separator


"""
This fill will cover the built in functions in Python. Focusing on Python 3.
Documentation can be found here:
https://docs.python.org/3/library/functions.html#abs
"""


separator("abs(integer) - Absolute Value - Integer")
for number in range(-3, 4):
    abs_number = abs(number)
    print("abs({}) = {}".format(number, abs_number))


separator("abs(float) - Absolute Value - Floating Point")
for _ in range(6):
    # Generate a random float with a random sign
    float_ = random.random() * 5 * random.randint(-100, 100)
    abs_float = abs(float_)
    print("abs({}) = {}".format(float_, abs_float))

separator("abs(complex) - Absolute Value - Complex Numbers - Returns the absolute value of the magnitude of the "
          "complex number.")
for _ in range(6):
    # Generate a random complex number with a random sign
    complex_ = complex(0, random.random() * 5 * random.randint(-100, 100))
    abs_complex = abs(complex_)
    print("abs({}) = {}".format(complex_, abs_complex))


separator("all(iterable) - with all items iterable - Returns true if all elements are iterable (non empty)")
print(all([1, 2, 3, 4, 5]))


separator("all(iterable) - with non-iterable items - Returns false if any elements are non iterable (empty)")
print(all([1, 2, None, {}, 0]))


separator("any(iterable) - with any iterable items - Returns True")
print(any([None, {}, False, [], 'I am iterable!']))


separator("any(iterable) - with NO iterable items - Returns False")
print(any([None, {}, False, []]))


separator("ascii(object) - Return an ascii string that has the control characters escaped if possible.")
string_with_control_characters = "Hello\t\n\r This is fun"
print(string_with_control_characters)
print(ascii(string_with_control_characters))

separator("bin(int) - Convert an integer to a binary number with a leading 0b")
for i in range(-3, 4):
    print(bin(i))


class IntExample(object):
    def __init__(self, number_):
        self.number = number_

    # Note that this class has an __index__ method.
    def __index__(self):
        return int(self.number)


separator("bin(int-object) - Convert an object with an __index__ method into a binary number with a leading 0b")
for i in range(-3, 4):
    x = IntExample(i)
    # bin calls the __index__ method of IntExample
    print(bin(x))


separator("bool(x) - determine if the x value is True or False using the truth testing procedure")
# Truth Testing Procedure Explained - https://docs.python.org/3/library/stdtypes.html#truth
false_list = [None, False, 0, 0.0, 0j, Decimal(0), Fraction(0, 1), '', "", (), [], {}, set(), range(0)]
for false_value in false_list:
    test_results = bool(false_value)
    print("Value: {} evaluates to: {}".format(false_value, test_results))
print("All other values evaluate to: {}".format(bool(1)))


# There is a very good video talking about the inner workings of bytearray found
# here: https://www.youtube.com/watch?v=z9Hmys8ojno
separator("bytearray(source) - generate a bytearray object. - Integers")
# creates an actual array of bytes with value range 0 - 255
print(bytearray(range(0, 256)))

# There is a very good video talking about the inner workings of bytearray found
# here: https://www.youtube.com/watch?v=z9Hmys8ojno
separator("bytearray(source, encoding) - generate a bytearray object. - String")
# creates an actual array of bytes in the string that is passed.
print(bytearray("I love simplicity, don't you?", 'utf-8'))


separator("bytes(")

