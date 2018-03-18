#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from src.theory.patterns.builder.builder import CellPhone
from src.theory.patterns.builder.builder import CircuitBoard
from src.theory.patterns.builder.builder import CellularModule
from src.theory.patterns.builder.builder import Battery
from src.theory.patterns.builder.builder import Speakers
from src.theory.patterns.builder.builder import Screen
from src.theory.patterns.builder.builder import ExternalShell



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

    def test_mfg_del(self):
        cp = CellPhone()
        del cp.mfg
        self.assertTrue(not hasattr(cp, "mfg"))

    def test_mfg_set_get(self):
        cp = CellPhone()
        cp.mfg = "cellphone_mfg"
        self.assertEqual("cellphone_mfg", cp.mfg)

    def test_model_del(self):
        cp = CellPhone()
        del cp.model
        self.assertTrue(not hasattr(cp, "model"))

    def test_model_set_get(self):
        cp = CellPhone()
        cp.model = "cellphone_model"
        self.assertEqual("cellphone_model", cp.model)

    def test_circuit_board_del(self):
        cp = CellPhone()
        del cp.circuit_board
        self.assertTrue(not hasattr(cp, "circuit_board"))

    def test_circuit_board_set_get(self):
        cp = CellPhone()
        cp.circuit_board = "cellphone_circuit_board"
        self.assertEqual("cellphone_circuit_board", cp.circuit_board)

    def test_battery_del(self):
        cp = CellPhone()
        del cp.battery
        self.assertTrue(not hasattr(cp, "battery"))

    def test_battery_set_get(self):
        cp = CellPhone()
        cp.battery = "cellphone_battery"
        self.assertEqual("cellphone_battery", cp.battery)

    def test_speakers_del(self):
        cp = CellPhone()
        del cp.speakers
        self.assertTrue(not hasattr(cp, "speakers"))

    def test_speakers_set_get(self):
        cp = CellPhone()
        cp.speakers = "cellphone_speakers"
        self.assertEqual("cellphone_speakers", cp.speakers)

    def test_external_shell_del(self):
        cp = CellPhone()
        del cp.external_shell
        self.assertTrue(not hasattr(cp, "external_shell"))

    def test_external_shell_set_get(self):
        cp = CellPhone()
        cp.external_shell = "cellphone_external_shell"
        self.assertEqual("cellphone_external_shell", cp.external_shell)

    @staticmethod
    def build_circuit_board_price(price):
        return CircuitBoard('test_model', 'test_version', .1, .02, price)

    @staticmethod
    def build_cellular_module_price(price):
        return CellularModule('test_mfg', 'test_model', ['cell_band_1', 'cell_band_2'], .1, .02, price)

    @staticmethod
    def build_battery_price(price):
        return Battery('test_form', 'test_type', 5, 200, price)

    @staticmethod
    def build_speakers_price(price):
        return Speakers('test_brand', 'test_frequency', 2, .1, .02, price)

    @staticmethod
    def build_screen_price(price):
        return Screen(1000, 800, 14, 60, .1, .02, price)

    @staticmethod
    def build_external_shell_price(assembly_price, price):
        return ExternalShell('test_material', 150, 85, .5, 'test_drop_height', assembly_price, False, False, price)

    def test_total_price_no_parts(self):
        cp = CellPhone()
        self.assertEqual(0.0, cp.total_price)

    def test_total_price_all_zeros(self):
        cp = CellPhone()
        cp.circuit_board = TestCellPhone.build_circuit_board_price(0.0)
        cp.cellular_module = TestCellPhone.build_cellular_module_price(0.0)
        cp.battery = TestCellPhone.build_battery_price(0.0)
        cp.speakers = TestCellPhone.build_speakers_price(0.0)
        cp.screen = TestCellPhone.build_screen_price(0.0)
        cp.ExternalShell = TestCellPhone.build_external_shell_price(0.0, 0.0)
        self.assertEqual(0.0, cp.total_price)

    def test_total_price_all_ones(self):
        cp = CellPhone()
        cp.circuit_board = TestCellPhone.build_circuit_board_price(1.0)
        cp.cellular_module = TestCellPhone.build_cellular_module_price(1.0)
        cp.battery = TestCellPhone.build_battery_price(1.0)
        cp.speakers = TestCellPhone.build_speakers_price(1.0)
        cp.screen = TestCellPhone.build_screen_price(1.0)
        cp.external_shell = TestCellPhone.build_external_shell_price(1.0, 1.0)
        self.assertEqual(6.0, cp.total_price)

    def test_total_price_increment_each_component(self):
        cp = CellPhone()
        cp.circuit_board = TestCellPhone.build_circuit_board_price(1.0)
        self.assertEqual(1.0, cp.total_price)

        cp.cellular_module = TestCellPhone.build_cellular_module_price(1.0)
        self.assertEqual(2.0, cp.total_price)

        cp.battery = TestCellPhone.build_battery_price(1.0)
        self.assertEqual(3.0, cp.total_price)

        cp.speakers = TestCellPhone.build_speakers_price(1.0)
        self.assertEqual(4.0, cp.total_price)

        cp.screen = TestCellPhone.build_screen_price(1.0)
        self.assertEqual(5.0, cp.total_price)

        cp.external_shell = TestCellPhone.build_external_shell_price(0.0, 1.0)
        self.assertEqual(6.0, cp.total_price)

        cp.external_shell = TestCellPhone.build_external_shell_price(1.0, 1.0)
        self.assertEqual(6.0, cp.total_price)

    def test_assembled_price_all_empty(self):
        cp = CellPhone()
        # cp.circuit_board = TestCellPhone.build_circuit_board_price(1.0)
        # cp.cellular_module = TestCellPhone.build_cellular_module_price(1.0)
        # cp.battery = TestCellPhone.build_battery_price(1.0)
        # cp.speakers = TestCellPhone.build_speakers_price(1.0)
        # cp.screen = TestCellPhone.build_screen_price(1.0)
        # cp.external_shell = TestCellPhone.build_external_shell_price(1.0, 1.0)
        self.assertEqual(0.0, cp.assembled_price)

    def test_assembled_price_single_component_and_assembly_cost(self):
        cp = CellPhone()
        cp.circuit_board = TestCellPhone.build_circuit_board_price(1.0)
        cp.external_shell = TestCellPhone.build_external_shell_price(1.0, 1.0)
        self.assertEqual(3.0, cp.assembled_price)

if __name__ == "__main__":
    # execute only if run as a script
    unittest.main()
