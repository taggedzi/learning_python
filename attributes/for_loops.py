#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lp_utils import separator

"""
For loops depend on the items they loop through being iterable.
For an object to be iterable it must have a next method. In python 2 it is "next" in Python 3 it is "__next__"

For many of these examples there may be better ways to perform the operation using something other
than a for loop however, this file exists to show how to use for loops. So they will be used.
"""

separator("Print a range from 0 to 5")
for i in range(0, 5):
    print("{}".format(i))

separator( "Print the characters of a string one at a time, iterating through the string.")
number = "654,321.123"
for i in range(0, len(number)):
    print(number[i], end='')
    print("")

separator("Filter a string by looping through it and removing any non-numeric characters.")
clean_number = ''
for i in number:
    if i in "0123456789":
        clean_number = clean_number + i
print(clean_number)

separator("Use a for loop and a range to print even numbers.")
for i in range(0, 10, 2):
    print(i)

separator("Use continue in a for loop to skip any entries that are not 'spam'.")
breakfast = ['eggs', 'turkey', 'spam', 'pancakes']
for item in breakfast:
    if 'spam' is not item:
        continue
    print('I want {} for breakfast.'.format(item))

separator("Use break in a for loop stop the loop if it encounters 'spam'.")
breakfast = ['eggs', 'turkey', 'spam', 'pancakes']
for item in breakfast:
    if 'spam' is item:
        break
    print('I want {} for breakfast.'.format(item))

separator("Use nested for loops to show multiplication table.")
for i in range(1, 10):
    for j in range(1, 10):
        print("{:<4}".format(j * i), end=" ")
    print("\n")

separator("Demonstrate the use of an else statement.")
for i in range(1, 3):
    print(i)
else:
    print('Finished loop without breaking')

separator("Demonstrate the use of an else statement when a break is triggered.")
for i in range(1, 10):
    print(i)
    break
else:
    print("This will never happen because of the break above.")

separator("Demonstrate what is happening under the hood using 'next' and 'iter'.")
demo = [1, 2, 3, 4, 5]
iter_ = demo.__iter__()
i = 0
while i <= 4:
    try:
        # python 3 way
        print(iter_.__next__())
    except AttributeError as _:
        # python 2 way
        print(iter_.next())
    i += 1
