#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from unittest.mock import Mock, patch, call
from src.theory.patterns.factories.factory_pattern import ShapeInterface, Circle, Square, ShapeFactory, main as fp_main


class TestFactoryPatternShapeInterface(unittest.TestCase):

    def test_shape_interface(self):
        si = ShapeInterface()
        si.draw()
        # If we got here... it worked.
        self.assertTrue(True)


class TestFactoryPatternCircle(unittest.TestCase):

    @patch('sys.stdout')
    def test_circle(self, mock_print):
        ci = Circle()
        ci.draw()
        expected = [call.write('Draw Circle')]
        mock_print.assert_has_calls(expected, any_order=True)


class TestFactoryPatternSquare(unittest.TestCase):

    @patch('sys.stdout')
    def test_square(self, mock_print):
        sq = Square()
        sq.draw()
        expected = [call.write('Draw Square')]
        mock_print.assert_has_calls(expected, any_order=True)


class TestFactoryPatternShapeFactory(unittest.TestCase):

    def test_no_type(self):
        with self.assertRaises(TypeError) as context:
            sf = ShapeFactory()
            sf.get_shape()
        self.assertTrue("get_shape() missing 1 required positional argument: 'type_'" in context.exception.args[0])

    def test_bad_type(self):
        with self.assertRaises(TypeError) as context:
            sf = ShapeFactory()
            sf.get_shape('orange')
        self.assertTrue("Type must be circle or square." == context.exception.args[0])


    def test_circle(self):
        sf = ShapeFactory()
        ci = sf.get_shape('circle')
        self.assertTrue(type(ci) is Circle)

    def test_square(self):
        sf = ShapeFactory()
        sq = sf.get_shape('square')
        self.assertTrue(type(sq) is Square)


class TestFactoryPatternMain(unittest.TestCase):

    @patch('src.theory.patterns.factories.factory_pattern.ShapeFactory')
    def test_main_pass(self, mock_factory):
        fp_main()
        expected = [call(),
                    call().get_shape('square'),
                    call().get_shape().draw(),
                    call().get_shape('circle'),
                    call().get_shape().draw(),
                    call().get_shape('hexagon'),
                    call().get_shape().draw()]
        mock_factory.assert_has_calls(expected)

    def return_type_error(self):
        raise TypeError('test')

    @patch('sys.stdout')
    @patch('src.theory.patterns.factories.factory_pattern.ShapeFactory.get_shape')
    def test_main_with_excpetion(self, mock_factory, mock_print):
        mock_factory.side_effect = [Square(), Circle(), TypeError('test')]
        fp_main()
        expected = [call.write('test')]
        mock_print.assert_has_calls(expected, any_order=True)


if __name__ == "__main__":
    unittest.main()
