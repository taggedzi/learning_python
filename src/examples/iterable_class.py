#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is an example of what is required to make an object Iterable

The object at minimum requires the '__iter__' method and the '__next__' method ('next' in python 2)

The '__iter__' methed should return the object it self
The '__next__' method should return the next item in the iteration and should raise a stop iteration exception when done

For more information about The Iteration Protocol
* The Iterator Protocol - https://anandology.com/python-practice-book/iterators.html#the-iteration-protocol
"""


class IterableExample(object):

    def __init__(self, limit):
        self.i = 0
        self.limit = limit

    def __iter__(self):
        return self

    # Note that this class has an '__next__' method. in python 2 it should be 'next'.
    def __next__(self):
        self.i += 1
        if self.i <= self.limit:
            return self.i
        else:
            raise StopIteration


for i in IterableExample(5):
    print(i)
