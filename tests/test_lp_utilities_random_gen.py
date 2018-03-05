#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import unittest.mock
from src.lp_utilities.random_gen import random_signed_float
from src.lp_utilities.random_gen import random_signed_integer
from src.lp_utilities.random_gen import random_signed_complex


class TestRandomGen(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_random_signed_float_no_input(self):
        with self.assertRaises(TypeError) as context:
            random_signed_float()
        self.assertTrue(
            "random_signed_float() missing 1 required positional argument: 'magnitude'" in context.exception.args[0])

    def test_random_signed_float_pass(self):
        answer = random_signed_float(0)
        self.assertEqual(0.0, answer)
        answer_1 = random_signed_float(1)
        self.assertTrue(abs(answer_1) <= 1)

    def test_random_signed_integer_no_input(self):
        with self.assertRaises(TypeError) as context:
            random_signed_integer()
        self.assertTrue(
            "random_signed_integer() missing 1 required positional argument: 'magnitude'" in context.exception.args[0])

    def test_random_signed_integer_pass(self):
        answer = random_signed_integer(0)
        self.assertEqual(0, answer)
        answer_1 = random_signed_integer(10)
        self.assertTrue(abs(answer_1) <= 10)

    def test_random_signed_complex_no_input(self):
        with self.assertRaises(TypeError) as context:
            random_signed_complex()
        self.assertTrue(
            "random_signed_complex() missing 1 required positional argument: 'magnitude'" in context.exception.args[0])

    def test_random_signed_complex_pass(self):
        answer = random_signed_complex(0)
        self.assertEqual(0j, answer)
        answer_1 = random_signed_complex(10)
        self.assertTrue(abs(answer_1) <= 10)
