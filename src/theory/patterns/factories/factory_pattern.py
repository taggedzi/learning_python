#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file contains a very simple example of a factory pattern.
You require at least:
1. Interface that defines the methods to be shared by all the created objects
2. At lease 1 object which implements the interface and will be constructed
3. A Factory class that generates the objects in question

You would want to use this type of pattern IF you won't know what class you
need to generate UNTIL runtime.
"""


class ShapeInterface(object):
    def draw(self): pass


class Circle(ShapeInterface):
    def draw(self):
        print('Draw Circle')


class Square(ShapeInterface):
    def draw(self):
        print('Draw Square')


class ShapeFactory(object):
    @staticmethod
    def get_shape(type_):
        if type_ == 'circle':
            return Circle()
        if type_ == 'square':
            return Square()
        raise TypeError('Type must be circle or square.')


def main():
    factory = ShapeFactory()

    square = factory.get_shape('square')
    square.draw()

    circle = factory.get_shape('circle')
    circle.draw()

    try:
        hexagon = factory.get_shape('hexagon')
        hexagon.draw()
    except TypeError as te:
        print(str(te))


if __name__ == "__main__":  # pragma: no cover
    # execute only if run as a script
    main()
