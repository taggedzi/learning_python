#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decimal import Decimal
from fractions import Fraction
from src.lp_utilities.separator import separator

"""
The any() function is a simple tests to see if any of the items in an iterable
contain an element that evaluates to false.

For more information on what an iterable object is
* The Iterator Protocol - https://anandology.com/python-practice-book/iterators.html#the-iteration-protocol

For more information on what evaluates to True in Python see:
* Truth Testing Procedure Explained - https://docs.python.org/3/library/stdtypes.html#truth
"""


def any_list_with_a_single_non_falsy_value():
    separator("any(iterable) - with any iterable items - Returns True")
    print(any(
        [None, False, 0, 0.0, 0j, Decimal(0), Fraction(0, 1), '', (), [], {}, set(), range(0), "I am not iterable."]))


def any_list_with_all_falsy_values():
    separator("any(iterable) - with NO iterable items - Returns False")
    print(any([None, False, 0, 0.0, 0j, Decimal(0), Fraction(0, 1), '', (), [], {}, set(), range(0)]))


def main():
    any_list_with_a_single_non_falsy_value()
    any_list_with_all_falsy_values()


if __name__ == '__main__':  # pragma: no cover
    # execute only if run as a script
    main()
