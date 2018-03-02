#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lp_utils import separator


"""
While loops are a basic program mechanism that loop until some condition is met, and then stops.

condition = True
while condition:
    statement_1
    statement_2
    statement_n
    condition = False
else:
    # Only Executed if while loop was NOT terminated with a break statement.
    statement_1
    statement_2
    statement_n

The above while loop will loop UNTIL the condition statement is False. So, If you never have a false
condition it will loop infinitely. IF the condition is NEVER TRUE... it will not execute any code
in the while loop.
"""

separator("Basic While loop example.")
index = 0
while index <= 5:
    print('There are {} flower peddles on the floor.'.format(index))
    index += 1


separator("More Advanced While Loop with user input")
condition = True
print('Oh how I love thee...')
while condition:
    loved = str(input("Doest thou love me in return? (y/n) "))
    if loved is 'y':
        print('Ever I love thee...')
    else:
        condition = False
else:
    print('Though thou doest cast away my love... ever I shall love thee... fair thee well.')


# I know in this example we could skip the check for even with the IF, however
# it was a quick an easy way to demonstrate a continue.
separator("While loop with a break in it")
index = 0
while index <= 50:
    # Note if the index is below our continue statement... this becomes an infinite loop
    index += 1

    if index % 2 == 0:
        # For some reason our boss is afraid of even numbers... so we skip all of them.
        continue

    if index != 7 and index % 7 == 0:
        print("We have found a multiple of 7 it is: {}".format(index))
        break
else:
    print("I will never be run.")


separator("Demonstrate how to iterate over an iterable object 'next' and 'iter'.")
demo = [1, 2, 3, 4, 5]
iter_ = demo.__iter__()
i = 0
while i <= len(demo) - 1:
    try:
        # python 3 way
        print(iter_.__next__())
    except AttributeError as _:
        # python 2 way
        print(iter_.next())
    i += 1
