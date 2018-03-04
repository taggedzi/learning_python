#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lp_utilities.separator import separator


"""
The "all()" function simply tests to see if ALL of the elements in an iterable evaluate to a True condition

For more information on what an iterable object is
* The Iterator Protocol - https://anandology.com/python-practice-book/iterators.html#the-iteration-protocol

For more information on what evaluates to True in Python see:
* Truth Testing Procedure Explained - https://docs.python.org/3/library/stdtypes.html#truth
"""


def print_all(input_, result_):
    print("Running all({}) returns {}".format(input_, result_))


def all_list_with_all_good_elements():
    # Demo a list of values that evaluate to true
    separator("all(iterable) - with all items iterable - Returns true if all elements are iterable (non empty)")
    good_list = [1, 2, 3, 4, 5, 'Cat', {'Carbon'}, ["Bacon"]]
    result = all(good_list)
    print_all(good_list, result)


def all_list_with_empty_element():
    # Demo a list with 1 value that evaluates to false
    separator("all(iterable) - with non-iterable items - Returns false if any elements are non iterable (empty)")
    bad_list = [1, 2, None, 4, 5]
    result = all(bad_list)
    print_all(bad_list, result)


def main():
    all_list_with_all_good_elements()
    all_list_with_empty_element()


if __name__ == "__main__":
    # execute only if run as a script
    main()
