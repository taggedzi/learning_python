#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Decorator takes a function as a parameter and adds functionality to the second function without explicitly modifying it.
"""


def p_decorate(func):
    """
    Simple decorator
    :param func: The function that the decorator encapsulates
    :return: the functions output wrapped by p tags
    """
    def func_wrapper(*args, **kwargs):
        return "<p>{f}</p>".format(f=func(*args, **kwargs))

    # Notice the return function is NOT executed there are no ()
    return func_wrapper


@p_decorate
def some_text(name):
    """
    Some method that doesn't even know about the decorator
    :param name: string some name
    :return: Some ipsum with a name
    """
    return "Ipsum {n}, Ipsum!".format(n=name)


def tag(tag_name):
    """
    A Decorator function that takes parameters
    :param tag_name: Str the html tag to use
    :return: the output of a function wrapped in a custom tag
    """
    def tag_decorator(func):
        """
        This function catches the function to be wrapped
        :param func: The function getting wrapped
        :return: A string with html tags
        """
        def func_wrapper(*args, **kwargs):
            """
            This function actually executes the function and then wraps the output with
            html tags.
            :param args:
            :param kwargs:
            :return:
            """
            return "<{t}>{f}</{t}>".format(t=tag_name, f=func(*args, **kwargs))
        return func_wrapper
    return tag_decorator


@tag('h1')
def some_text_2(name):
    return "I knew {n} could get the job done!".format(n=name)


def main():
    print(some_text("John Wanye"))
    print(some_text_2("Superman"))


if __name__ == "__main__":
    # execute only if run as a script
    main()
