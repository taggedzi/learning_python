#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from src.theory.patterns.builder.builder import CellPhone


class ComponentTestClassEmpty(object):
    pass


class ComponentTestClassWithPrice(object):
    def __init__(self, price):
        self.price = price


class ComponentTestClassWithPassiveDraw(object):
    def __init__(self, draw):
        self.passive_draw = draw


class ComponentTestClassWithActiveDraw(object):
    def __init__(self, draw):
        self.active_draw = draw


class TestCellPhone(unittest.TestCase):

    def test_convert_seconds_no_input_exception(self):
        with self.assertRaises(TypeError) as context:
            CellPhone.convert_seconds(None)
        self.assertTrue("unsupported operand type(s) for divmod(): 'NoneType' and 'int'" in context.exception.args[0])

    def test_convert_seconds_zero(self):
        days, hours, minutes, seconds = CellPhone.convert_seconds(0)
        self.assertEqual(0, days)
        self.assertEqual(0, hours)
        self.assertEqual(0, minutes)
        self.assertEqual(0, seconds)

    def test_convert_seconds_10(self):
        days, hours, minutes, seconds = CellPhone.convert_seconds(10)
        self.assertEqual(0, days)
        self.assertEqual(0, hours)
        self.assertEqual(0, minutes)
        self.assertEqual(10, seconds)

    def test_convert_seconds_61(self):
        days, hours, minutes, seconds = CellPhone.convert_seconds(61)
        self.assertEqual(0, days)
        self.assertEqual(0, hours)
        self.assertEqual(1, minutes)
        self.assertEqual(1, seconds)

    def test_convert_seconds_3661(self):
        days, hours, minutes, seconds = CellPhone.convert_seconds(3661)
        self.assertEqual(0, days)
        self.assertEqual(1, hours)
        self.assertEqual(1, minutes)
        self.assertEqual(1, seconds)

    def test_convert_seconds_90061(self):
        days, hours, minutes, seconds = CellPhone.convert_seconds(90061)
        self.assertEqual(1, days)
        self.assertEqual(1, hours)
        self.assertEqual(1, minutes)
        self.assertEqual(1, seconds)

    def test_get_price_not_set(self):
        component = ComponentTestClassEmpty()
        answer = CellPhone.get_price(component)
        self.assertEqual(0, answer)

    def test_get_price_set(self):
        component = ComponentTestClassWithPrice(1)
        answer = CellPhone.get_price(component)
        self.assertEqual(1, answer)

    def test_calculate_msrp(self):
        answer = CellPhone.calculate_msrp(1)
        self.assertEqual(2.5, answer)

    def test_passive_current_draw_not_set(self):
        component = ComponentTestClassEmpty()
        answer = CellPhone.get_passive_current_draw(component)
        self.assertEqual(0, answer)

    def test_passive_current_draw_set(self):
        component = ComponentTestClassWithPassiveDraw(1.8)
        answer = CellPhone.get_passive_current_draw(component)
        self.assertEqual(1.8, answer)

    def test_active_current_draw_not_set(self):
        component = ComponentTestClassEmpty()
        answer = CellPhone.get_active_current_draw(component)
        self.assertEqual(0, answer)

    def test_active_current_draw_set(self):
        component = ComponentTestClassWithActiveDraw(1.8)
        answer = CellPhone.get_active_current_draw(component)
        self.assertEqual(1.8, answer)

    def test_convert_hours_to_seconds(self):
        answer = CellPhone.convert_hours_to_seconds(1)
        self.assertEqual(60 * 60, answer)

    def test_mfg_get_set_del(self):
        cp = CellPhone()
        cp.mfg = ''


if __name__ == "__main__":
    # execute only if run as a script
    unittest.main()
