#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch
from unittest.mock import Mock
from src.theory.patterns.builder.builder import CellPhone
from src.theory.patterns.builder.builder import CircuitBoard
from src.theory.patterns.builder.builder import CellularModule
from src.theory.patterns.builder.builder import Battery
from src.theory.patterns.builder.builder import Speakers
from src.theory.patterns.builder.builder import Screen
from src.theory.patterns.builder.builder import ExternalShell
from src.theory.patterns.builder.builder import Director
from src.theory.patterns.builder.builder import MeFone12
from src.theory.patterns.builder.builder import BirdSungT8


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

    def __init__(self, *args, **kwargs):
        super(TestCellPhone, self).__init__(*args, **kwargs)
        self.maxDiff = None
        self.cp = None

    def setUp(self):
        self.cp = CellPhone()

    def tearDown(self):
        del self.cp

    @staticmethod
    def build_battery_with_mah(mah):
        return Battery('test_form', 'test_type', mah, 200, 3)

    @staticmethod
    def build_external_shell():
        return ExternalShell('test_material', 150, 85, .5, 'test_drop_height', 3, False, False, 3)

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

    @staticmethod
    def build_circuit_board_passive_battery_duration(passive):
        return CircuitBoard('test_model', 'test_version', .1, passive, 3)

    @staticmethod
    def build_cellular_module_passive_battery_duration(passive):
        return CellularModule('test_mfg', 'test_model', ['cell_band_1', 'cell_band_2'], .1, passive, 3)

    @staticmethod
    def build_speakers_passive_battery_duration(passive):
        return Speakers('test_brand', 'test_frequency', 2, .1, passive, 3)

    @staticmethod
    def build_screen_passive_battery_duration(passive):
        return Screen(1000, 800, 14, 60, .1, passive, 3)

    @staticmethod
    def build_circuit_board_active_battery_duration(active):
        return CircuitBoard('test_model', 'test_version', active, 0.02, 3)

    @staticmethod
    def build_cellular_module_active_battery_duration(active):
        return CellularModule('test_mfg', 'test_model', ['cell_band_1', 'cell_band_2'], active, 0.02, 3)

    @staticmethod
    def build_speakers_active_battery_duration(active):
        return Speakers('test_brand', 'test_frequency', 2, active, 0.02, 3)

    @staticmethod
    def build_screen_active_battery_duration(active):
        return Screen(1000, 800, 14, 60, active, 0.02, 3)

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
        del self.cp.mfg
        self.assertTrue(not hasattr(self.cp, "mfg"))

    def test_mfg_set_get(self):
        self.cp.mfg = "cellphone_mfg"
        self.assertEqual("cellphone_mfg", self.cp.mfg)

    def test_model_del(self):
        del self.cp.model
        self.assertTrue(not hasattr(self.cp, "model"))

    def test_model_set_get(self):
        self.cp.model = "cellphone_model"
        self.assertEqual("cellphone_model", self.cp.model)

    def test_circuit_board_del(self):
        del self.cp.circuit_board
        self.assertTrue(not hasattr(self.cp, "circuit_board"))

    def test_circuit_board_set_get(self):
        self.cp.circuit_board = "cellphone_circuit_board"
        self.assertEqual("cellphone_circuit_board", self.cp.circuit_board)

    def test_cellular_module_del(self):
        del self.cp.cellular_module
        self.assertTrue(not hasattr(self.cp, "cellular_module"))

    def test_cellular_module_set_get(self):
        self.cp.cellular_module = "cellphone_cellular_module"
        self.assertEqual("cellphone_cellular_module", self.cp.cellular_module)

    def test_battery_del(self):
        del self.cp.battery
        self.assertTrue(not hasattr(self.cp, "battery"))

    def test_battery_set_get(self):
        self.cp.battery = "cellphone_battery"
        self.assertEqual("cellphone_battery", self.cp.battery)

    def test_speakers_del(self):
        del self.cp.speakers
        self.assertTrue(not hasattr(self.cp, "speakers"))

    def test_speakers_set_get(self):
        self.cp.speakers = "cellphone_speakers"
        self.assertEqual("cellphone_speakers", self.cp.speakers)

    def test_screen_del(self):
        del self.cp.screen
        self.assertTrue(not hasattr(self.cp, "screen"))

    def test_screen_set_get(self):
        self.cp.screen = "cellphone_screen"
        self.assertEqual("cellphone_screen", self.cp.screen)

    def test_external_shell_del(self):
        del self.cp.external_shell
        self.assertTrue(not hasattr(self.cp, "external_shell"))

    def test_external_shell_set_get(self):
        self.cp.external_shell = "cellphone_external_shell"
        self.assertEqual("cellphone_external_shell", self.cp.external_shell)

    def test_total_price_no_parts(self):
        self.assertEqual(0.0, self.cp.total_price)

    def test_total_price_all_zeros(self):
        self.cp.circuit_board = TestCellPhone.build_circuit_board_price(0.0)
        self.cp.cellular_module = TestCellPhone.build_cellular_module_price(0.0)
        self.cp.battery = TestCellPhone.build_battery_price(0.0)
        self.cp.speakers = TestCellPhone.build_speakers_price(0.0)
        self.cp.screen = TestCellPhone.build_screen_price(0.0)
        self.cp.external_shell = TestCellPhone.build_external_shell_price(0.0, 0.0)
        self.assertEqual(0.0, self.cp.total_price)

    def test_total_price_all_ones(self):
        self.cp.circuit_board = TestCellPhone.build_circuit_board_price(1.0)
        self.cp.cellular_module = TestCellPhone.build_cellular_module_price(1.0)
        self.cp.battery = TestCellPhone.build_battery_price(1.0)
        self.cp.speakers = TestCellPhone.build_speakers_price(1.0)
        self.cp.screen = TestCellPhone.build_screen_price(1.0)
        self.cp.external_shell = TestCellPhone.build_external_shell_price(1.0, 1.0)
        self.assertEqual(6.0, self.cp.total_price)

    def test_total_price_increment_each_component(self):
        self.cp.circuit_board = TestCellPhone.build_circuit_board_price(1.0)
        self.assertEqual(1.0, self.cp.total_price)

        self.cp.cellular_module = TestCellPhone.build_cellular_module_price(1.0)
        self.assertEqual(2.0, self.cp.total_price)

        self.cp.battery = TestCellPhone.build_battery_price(1.0)
        self.assertEqual(3.0, self.cp.total_price)

        self.cp.speakers = TestCellPhone.build_speakers_price(1.0)
        self.assertEqual(4.0, self.cp.total_price)

        self.cp.screen = TestCellPhone.build_screen_price(1.0)
        self.assertEqual(5.0, self.cp.total_price)

        self.cp.external_shell = TestCellPhone.build_external_shell_price(0.0, 1.0)
        self.assertEqual(6.0, self.cp.total_price)

        self.cp.external_shell = TestCellPhone.build_external_shell_price(1.0, 1.0)
        self.assertEqual(6.0, self.cp.total_price)

    def test_assembled_price_all_empty(self):
        self.assertEqual(0.0, self.cp.assembled_price)

    def test_assembled_price_single_component_and_assembly_cost(self):
        self.cp.circuit_board = TestCellPhone.build_circuit_board_price(1.0)
        self.cp.external_shell = TestCellPhone.build_external_shell_price(1.0, 1.0)
        self.assertEqual(3.0, self.cp.assembled_price)

    def test_passive_battery_duration_no_components_set(self):
        self.cp.circuit_board = TestCellPhone.build_circuit_board_passive_battery_duration(0.0)
        self.cp.cellular_module = TestCellPhone.build_cellular_module_passive_battery_duration(0.0)
        self.cp.battery = TestCellPhone.build_battery_with_mah(0.0)
        self.cp.speakers = TestCellPhone.build_speakers_passive_battery_duration(0.0)
        self.cp.screen = TestCellPhone.build_screen_passive_battery_duration(0.0)
        self.cp.external_shell = TestCellPhone.build_external_shell()
        self.assertEqual((0, 0, 0, 0), self.cp.passive_battery_duration)

    def test_passive_battery_duration_all_components_set_no_battery(self):
        self.cp.circuit_board = TestCellPhone.build_circuit_board_passive_battery_duration(.02)
        self.cp.cellular_module = TestCellPhone.build_cellular_module_passive_battery_duration(.02)
        self.cp.battery = TestCellPhone.build_battery_with_mah(0.0)
        self.cp.speakers = TestCellPhone.build_speakers_passive_battery_duration(0.2)
        self.cp.screen = TestCellPhone.build_screen_passive_battery_duration(0.2)
        self.cp.external_shell = TestCellPhone.build_external_shell()
        self.assertEqual((0, 0, 0, 0), self.cp.passive_battery_duration)

    def test_passive_battery_duration_all_components_set(self):
        self.cp.circuit_board = TestCellPhone.build_circuit_board_passive_battery_duration(.02)
        self.cp.cellular_module = TestCellPhone.build_cellular_module_passive_battery_duration(.02)
        self.cp.battery = TestCellPhone.build_battery_with_mah(2)
        self.cp.speakers = TestCellPhone.build_speakers_passive_battery_duration(0.2)
        self.cp.screen = TestCellPhone.build_screen_passive_battery_duration(0.2)
        self.cp.external_shell = TestCellPhone.build_external_shell()
        self.assertEqual((0, 8, 20, 0), self.cp.passive_battery_duration)

    def test_active_battery_duration_no_components_set(self):
        self.cp.circuit_board = TestCellPhone.build_circuit_board_active_battery_duration(0.0)
        self.cp.cellular_module = TestCellPhone.build_cellular_module_active_battery_duration(0.0)
        self.cp.battery = TestCellPhone.build_battery_with_mah(0.0)
        self.cp.speakers = TestCellPhone.build_speakers_active_battery_duration(0.0)
        self.cp.screen = TestCellPhone.build_screen_active_battery_duration(0.0)
        self.cp.external_shell = TestCellPhone.build_external_shell()
        self.assertEqual((0, 0, 0, 0), self.cp.active_battery_duration)

    def test_active_battery_duration_all_components_set_no_battery(self):
        self.cp.circuit_board = TestCellPhone.build_circuit_board_active_battery_duration(.1)
        self.cp.cellular_module = TestCellPhone.build_cellular_module_active_battery_duration(.1)
        self.cp.battery = TestCellPhone.build_battery_with_mah(0.0)
        self.cp.speakers = TestCellPhone.build_speakers_active_battery_duration(0.1)
        self.cp.screen = TestCellPhone.build_screen_active_battery_duration(0.1)
        self.cp.external_shell = TestCellPhone.build_external_shell()
        self.assertEqual((0, 0, 0, 0), self.cp.active_battery_duration)

    def test_active_battery_duration_all_components_set(self):
        self.cp.circuit_board = TestCellPhone.build_circuit_board_active_battery_duration(.1)
        self.cp.cellular_module = TestCellPhone.build_cellular_module_active_battery_duration(.1)
        self.cp.battery = TestCellPhone.build_battery_with_mah(2)
        self.cp.speakers = TestCellPhone.build_speakers_active_battery_duration(0.1)
        self.cp.screen = TestCellPhone.build_screen_active_battery_duration(0.1)
        self.cp.external_shell = TestCellPhone.build_external_shell()
        self.assertEqual((0, 8, 20, 0), self.cp.active_battery_duration)

    @patch("sys.stdout", Mock())
    def test_brochure(self):
        self.cp.circuit_board = TestCellPhone.build_circuit_board_active_battery_duration(.1)
        self.cp.cellular_module = TestCellPhone.build_cellular_module_active_battery_duration(.1)
        self.cp.battery = TestCellPhone.build_battery_with_mah(2)
        self.cp.speakers = TestCellPhone.build_speakers_active_battery_duration(0.1)
        self.cp.screen = TestCellPhone.build_screen_active_battery_duration(0.1)
        self.cp.external_shell = TestCellPhone.build_external_shell()

        result = """--------------------------------------------------------------------------------
Manufacturer: None; Model: None
Primary board design: test_model vtest_version
Supported cellular bands: ['cell_band_1', 'cell_band_2']
Battery: Capacity: 2 mAH;
\tEstimated standby time: (0, 8, 20, 0) days, hours, minutes, seconds;
\tEstimated talk time: (0, 8, 20, 0) days, hours, minutes, seconds;
Speakers response frequency: test_frequency
Screen resolution: 11200x14000 @ 60 hz
External Dimensions: Height 150 mm, Width 85 mm, Depth 0.5 mm.
MSRP: $45.00;
"""
        self.assertEqual(result, self.cp.brochure)

    def test_string_conversion(self):
        self.cp.circuit_board = TestCellPhone.build_circuit_board_active_battery_duration(.1)
        self.cp.cellular_module = TestCellPhone.build_cellular_module_active_battery_duration(.1)
        self.cp.battery = TestCellPhone.build_battery_with_mah(2)
        self.cp.speakers = TestCellPhone.build_speakers_active_battery_duration(0.1)
        self.cp.screen = TestCellPhone.build_screen_active_battery_duration(0.1)
        self.cp.external_shell = TestCellPhone.build_external_shell()

        result = """Manufacturer: None; Model: None;
Circuit Board:
\tModel: test_model vtest_version
\tPower Consumption:
\t\tMax: 0.1 mA; Min 0.02 mA;
\tPrice: $3.00 USD
Cellular Module:
\tManufacturer: test_mfg; Make: test_model;
\tSupported Cellular Protocols: ['cell_band_1', 'cell_band_2']
\tPower Consumption:
\t\tMax: 0.1 mA; Min 0.02 mA;
\tPrice: $3.00 USD
Battery:
\tForm factor: test_form
\tBattery type: test_type
\tStorage Capacity: 2 mAh; Average Charging Cycles: 200;
\tPrice: $3.00 USD;
Speakers:
\tBrand: test_brand
\tResponse Frequency: test_frequency
\tElectrical Specs:
\t\tImpedance: 2
\t\tMax Current Draw: 0.02 mA; Min Current Draw: 0.1 mA
\tPrice: $3.00 USD
Screen:
\tDimensions:
\t\tHeight: 1000 mm; Width: 800 mm
\tDisplay Details:
\t\tHeight in pixels: 14000;
\t\tWidth in pixels: 11200;
\t\tPixel Density (ppmm): 14;
\t\tRefresh Rate: 60
\tCurrent Draw:
\t\tMax Current Draw: 0.02 mA; Min Current Draw: 0.1 mA
\tPrice: $3.00 USD
External Shell:
\tConstruction Material: test_material;
\tDimensions:
\t\tHeight: 150 mm; Width: 85 mm; Depth: 0.5 mm;
\tDrop Resistance: test_drop_height;
\tWater Proof: False;
\tDust and Sand Proof: False;
\tPrice: $3.00 USD;
\tAssembly Cost: $3.00;
Price of Parts: $18.00 USD;
Assembled Price: $21.00 USD;
Recommended MSRP: $45.00 USD;
"""
        self.assertEqual(result, str(self.cp))


class TestCircuitBoard(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestCircuitBoard, self).__init__(*args, **kwargs)
        self.cb = None
        self.test_model = 'test_model'
        self.test_revision = 'test_revision'
        self.test_active_draw = 0.1
        self.test_passive_draw = 0.02
        self.test_price = 5.00

    def setUp(self):
        self.cb = CircuitBoard(self.test_model, self.test_revision, self.test_active_draw, self.test_passive_draw,
                               self.test_price)

    def test_init(self):
        self.assertEqual(self.test_model, self.cb.model)
        self.assertEqual(self.test_revision, self.cb.revision)
        self.assertEqual(self.test_active_draw, self.cb.active_draw)
        self.assertEqual(self.test_passive_draw, self.cb.passive_draw)
        self.assertEqual(self.test_price, self.cb.price)

    def test_string_conversion(self):
        expected = "Circuit Board:\n"
        expected += "\tModel: {self.test_model} v{self.test_revision}\n".format(self=self)
        expected += "\tPower Consumption:\n"
        expected += "\t\tMax: {self.test_active_draw} mA; Min {self.test_passive_draw} mA;\n".format(self=self)
        expected += "\tPrice: ${self.test_price:.2f} USD\n".format(self=self)
        self.assertEqual(expected, str(self.cb))


class TestCelluarModule(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestCelluarModule, self).__init__(*args, **kwargs)
        self.cm = None
        self.test_manufacturer = 'test_manufacturer'
        self.test_make = 'test_make'
        self.test_bands = ['cell_band_1', 'cell_band_2']
        self.test_active_draw = 0.1
        self.test_passive_draw = 0.02
        self.test_price = 5.00

    def setUp(self):
        self.cm = CellularModule(self.test_manufacturer, self.test_make, self.test_bands, self.test_active_draw,
                                 self.test_passive_draw, self.test_price)

    def test_init(self):
        self.assertEqual(self.test_manufacturer, self.cm.manufacturer)
        self.assertEqual(self.test_make, self.cm.make)
        self.assertEqual(self.test_bands, self.cm.bands)
        self.assertEqual(self.test_active_draw, self.cm.active_draw)
        self.assertEqual(self.test_passive_draw, self.cm.passive_draw)
        self.assertEqual(self.test_price, self.cm.price)

    def test_string_conversion(self):
        expected = "Cellular Module:\n"
        expected += "\tManufacturer: {self.test_manufacturer}; Make: {self.test_make};\n".format(self=self)
        expected += "\tSupported Cellular Protocols: {self.test_bands}\n".format(self=self)
        expected += "\tPower Consumption:\n"
        expected += "\t\tMax: {self.test_active_draw} mA; Min {self.test_passive_draw} mA;\n".format(self=self)
        expected += "\tPrice: ${self.test_price:.2f} USD\n".format(self=self)
        self.assertEqual(expected, str(self.cm))


class TestBattery(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestBattery, self).__init__(*args, **kwargs)
        self.b = None
        self.test_form_factor = 'test_form_factor'
        self.test_battery_type = 'test_battery_type'
        self.test_storage_capacity = 2
        self.test_charge_cycles = 300
        self.test_price = 5.00

    def setUp(self):
        self.b = Battery(self.test_form_factor, self.test_battery_type, self.test_storage_capacity, self.test_charge_cycles,
                         self.test_price)

    def test_init(self):
        self.assertEqual(self.test_form_factor, self.b.form_factor)
        self.assertEqual(self.test_battery_type, self.b.battery_type)
        self.assertEqual(self.test_storage_capacity, self.b.storage_capacity)
        self.assertEqual(self.test_charge_cycles, self.b.charge_cycles)
        self.assertEqual(self.test_price, self.b.price)

    def test_string_conversion(self):
        expected = "Battery:\n"
        expected += "\tForm factor: {self.test_form_factor}\n".format(self=self)
        expected += "\tBattery type: {self.test_battery_type}\n".format(self=self)
        expected += "\tStorage Capacity: {self.test_storage_capacity} mAh; " \
                    "Average Charging Cycles: {self.test_charge_cycles};\n".format(self=self)
        expected += "\tPrice: ${self.test_price:.2f} USD;\n".format(self=self)
        self.assertEqual(expected, str(self.b))


class TestSpeakers(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSpeakers, self).__init__(*args, **kwargs)
        self.s = None
        self.test_brand = 'test_brand'
        self.test_response_frequency = 'test_response_frequency'
        self.test_impedance = 4
        self.test_passive_draw = 0.02
        self.test_active_draw = 0.1
        self.test_price = 5.00

    def setUp(self):
        self.s = Speakers(self.test_brand, self.test_response_frequency, self.test_impedance, self.test_passive_draw,
                          self.test_active_draw, self.test_price)

    def test_init(self):
        self.assertEqual(self.test_brand, self.s.brand)
        self.assertEqual(self.test_response_frequency, self.s.response_frequency)
        self.assertEqual(self.test_impedance, self.s.impedance)
        self.assertEqual(self.test_passive_draw, self.s.passive_draw)
        self.assertEqual(self.test_active_draw, self.s.active_draw)
        self.assertEqual(self.test_price, self.s.price)

    def test_string_conversion(self):
        expected = "Speakers:\n"
        expected += "\tBrand: {self.test_brand}\n".format(self=self)
        expected += "\tResponse Frequency: {self.test_response_frequency}\n".format(self=self)
        expected += "\tElectrical Specs:\n"
        expected += "\t\tImpedance: {self.test_impedance}\n".format(self=self)
        expected += "\t\tMax Current Draw: {self.test_active_draw} mA; " \
                    "Min Current Draw: {self.test_passive_draw} mA\n".format(self=self)
        expected += "\tPrice: ${self.test_price:.2f} USD\n".format(self=self)
        self.assertEqual(expected, str(self.s))


class TestScreen(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestScreen, self).__init__(*args, **kwargs)
        self.s = None
        self.test_height = 1080
        self.test_width = 768
        self.test_pixels_per_mm = 10
        self.test_refresh_rate = 24
        self.test_passive_draw = .1
        self.test_active_draw = .4
        self.test_price = 5.00
        self.calculated_height = self.test_height * self.test_pixels_per_mm
        self.calculated_width = self.test_width * self.test_pixels_per_mm

    def setUp(self):
        self.s = Screen(self.test_height, self.test_width, self.test_pixels_per_mm, self.test_refresh_rate,
                        self.test_passive_draw, self.test_active_draw, self.test_price)

    def test_init(self):
        self.assertEqual(self.test_height, self.s.height)
        self.assertEqual(self.test_width, self.s.width)
        self.assertEqual(self.test_pixels_per_mm, self.s.pixels_per_mm)
        self.assertEqual(self.test_height * self.test_pixels_per_mm, self.s.height_pixels)
        self.assertEqual(self.test_width * self.test_pixels_per_mm, self.s.width_pixels)
        self.assertEqual(self.test_refresh_rate, self.s.refresh_rate)
        self.assertEqual(self.test_passive_draw, self.s.passive_draw)
        self.assertEqual(self.test_active_draw, self.s.active_draw)
        self.assertEqual(self.test_price, self.s.price)
        self.assertEqual(self.calculated_height, self.s.height_pixels)
        self.assertEqual(self.calculated_width, self.s.width_pixels)

    def test_string_conversion(self):
        expected = "Screen:\n"
        expected += "\tDimensions:\n"
        expected += "\t\tHeight: {self.test_height} mm; Width: {self.test_width} mm\n".format(self=self)
        expected += "\tDisplay Details:\n"
        expected += "\t\tHeight in pixels: {self.calculated_height};\n".format(self=self)
        expected += "\t\tWidth in pixels: {self.calculated_width};\n".format(self=self)
        expected += "\t\tPixel Density (ppmm): {self.test_pixels_per_mm};\n".format(self=self)
        expected += "\t\tRefresh Rate: {self.test_refresh_rate}\n".format(self=self)
        expected += "\tCurrent Draw:\n"
        expected += "\t\tMax Current Draw: {self.test_active_draw} mA; " \
                    "Min Current Draw: {self.test_passive_draw} mA\n".format(self=self)
        expected += "\tPrice: ${self.test_price:.2f} USD\n".format(self=self)
        self.assertEqual(expected, str(self.s))


class TestExternalShell(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestExternalShell, self).__init__(*args, **kwargs)
        self.es = None
        self.test_material = "test_material"
        self.test_height = 768
        self.test_width = 1080
        self.test_depth = 5.5
        self.test_drop_resistance_rating = 4
        self.test_assembly_cost = 5.12
        self.test_is_water_proof = False
        self.test_is_dust_sand_proof = False
        self.test_price = 1.22

    def setUp(self):
        self.es = ExternalShell(self.test_material, self.test_height, self.test_width, self.test_depth,
                                self.test_drop_resistance_rating, self.test_assembly_cost, self.test_is_water_proof,
                                self.test_is_dust_sand_proof, self.test_price)

    def test_init(self):
        self.assertEqual(self.test_material, self.es.material)
        self.assertEqual(self.test_height, self.es.height)
        self.assertEqual(self.test_width, self.es.width)
        self.assertEqual(self.test_depth, self.es.depth)
        self.assertEqual(self.test_drop_resistance_rating, self.es.drop_resistance_rating)
        self.assertEqual(self.test_assembly_cost, self.es.assembly_cost)
        self.assertEqual(self.test_is_water_proof, self.es.is_water_proof)
        self.assertEqual(self.test_is_dust_sand_proof, self.es.is_dust_sand_proof)
        self.assertEqual(self.test_price, self.es.price)

    def test_string_conversion(self):
        expected = "External Shell:\n"
        expected += "\tConstruction Material: {self.test_material};\n".format(self=self)
        expected += "\tDimensions:\n"
        expected += "\t\tHeight: {self.test_height} mm; Width: {self.test_width} mm; Depth: {self.test_depth} mm;\n".format(self=self)
        expected += "\tDrop Resistance: {self.test_drop_resistance_rating};\n".format(self=self)
        expected += "\tWater Proof: {self.test_is_water_proof};\n".format(self=self)
        expected += "\tDust and Sand Proof: {self.test_is_dust_sand_proof};\n".format(self=self)
        expected += "\tPrice: ${self.test_price:.2f} USD;\n".format(self=self)
        expected += "\tAssembly Cost: ${self.test_assembly_cost:.2f};\n".format(self=self)
        self.assertEqual(expected, str(self.es))


class MockBuilder(object):
    mfg = "test_mfg"
    model = "test_model"

    def build_circuit_board(self):
        return "test_circuit_board"

    def build_cellular_module(self):
        return "test_cellular_module"

    def build_battery(self):
        return "test_battery"

    def build_speakers(self):
        return "test_speakers"

    def build_screen(self):
        return "test_screen"

    def build_external_shell(self):
        return "test_external_shell"


class TestDirector(unittest.TestCase):

    def test_build_phone(self):
        d = Director()
        d.set_builder(MockBuilder())
        phone = d.build_phone()
        self.assertEqual("test_mfg", phone.mfg)
        self.assertEqual("test_model", phone.model)
        self.assertEqual("test_circuit_board", phone.circuit_board)
        self.assertEqual("test_cellular_module", phone.cellular_module)
        self.assertEqual("test_battery", phone.battery)
        self.assertEqual("test_speakers", phone.speakers)
        self.assertEqual("test_screen", phone.screen)
        self.assertEqual("test_external_shell", phone.external_shell)


class TestMeFone12(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestMeFone12, self).__init__(*args, **kwargs)
        self.mf = None

    def setUp(self):
        self.mf = MeFone12()

    def test_init(self):
        self.assertEqual("NBD", self.mf.mfg)
        self.assertEqual("MeFone12", self.mf.model)

    def test_build_circuit_board(self):
        cb = self.mf.build_circuit_board()
        self.assertEqual('MRL-0032', cb.model)
        self.assertEqual('1.3.7a', cb.revision)
        self.assertEqual(.127, cb.active_draw)
        self.assertEqual(0.018, cb.passive_draw)
        self.assertEqual(98.79, cb.price)

    def test_build_cellular_module(self):
        cm = self.mf.build_cellular_module()
        self.assertEqual('Kellog', cm.manufacturer)
        self.assertEqual('ARNIL-3', cm.make)
        self.assertEqual(['3G', '4G', 'LTE'], cm.bands)
        self.assertEqual(0.118, cm.active_draw)
        self.assertEqual(0.006, cm.passive_draw)
        self.assertEqual(75.33, cm.price)

    def test_build_battery(self):
        b = self.mf.build_battery()
        self.assertEqual('M-004', b.form_factor)
        self.assertEqual('NiCAD', b.battery_type)
        self.assertEqual(8, b.storage_capacity)
        self.assertEqual(250, b.charge_cycles)
        self.assertEqual(5.38, b.price)

    def test_build_speakers(self):
        s = self.mf.build_speakers()
        self.assertEqual('Lanteek', s.brand)
        self.assertEqual('35 - 21 kHz', s.response_frequency)
        self.assertEqual(4, s.impedance)
        self.assertEqual(0.2, s.active_draw)
        self.assertEqual(0, s.passive_draw)
        self.assertEqual(5.00, s.price)

    def test_build_screen(self):
        s = self.mf.build_screen()
        self.assertEqual(158.4, s.height)
        self.assertEqual(78.1, s.width)
        self.assertEqual(17.78, s.pixels_per_mm)
        self.assertEqual(round(s.height * s.pixels_per_mm), s.height_pixels)
        self.assertEqual(round(s.width * s.pixels_per_mm), s.width_pixels)
        self.assertEqual(60, s.refresh_rate)
        self.assertEqual(0.3, s.passive_draw)
        self.assertEqual(0.68, s.active_draw)
        self.assertEqual(65.88, s.price)

    def test_build_external_shell(self):
        es = self.mf.build_external_shell()
        self.assertEqual('Aluminum', es.material)
        self.assertEqual(158.9, es.height)
        self.assertEqual(85.1, es.width)
        self.assertEqual(0.4, es.depth)
        self.assertEqual('3 ft.', es.drop_resistance_rating)
        self.assertEqual(12.10, es.assembly_cost)
        self.assertEqual(False, es.is_water_proof)
        self.assertEqual(False, es.is_dust_sand_proof)
        self.assertEqual(6.12, es.price)


class TestBirdSungT8(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestBirdSungT8, self).__init__(*args, **kwargs)
        self.bs8 = None

    def setUp(self):
        self.bs8 = BirdSungT8()

    def test_init(self):
        self.assertEqual("Birdsung", self.bs8.mfg)
        self.assertEqual("T8", self.bs8.model)

    def test_build_circuit_board(self):
        cb = self.bs8.build_circuit_board()
        self.assertEqual('Cobalt', cb.model)
        self.assertEqual('2.0.4', cb.revision)
        self.assertEqual(.117, cb.active_draw)
        self.assertEqual(0.021, cb.passive_draw)
        self.assertEqual(78.21, cb.price)

    def test_build_cellular_module(self):
        cm = self.bs8.build_cellular_module()
        self.assertEqual('LuckySnaps', cm.manufacturer)
        self.assertEqual('VINA99', cm.make)
        self.assertEqual(['3G', '4G', 'CDMA', 'FDMA', 'EVDO3'], cm.bands)
        self.assertEqual(0.21, cm.active_draw)
        self.assertEqual(0.008, cm.passive_draw)
        self.assertEqual(72.63, cm.price)

    def test_build_battery(self):
        b = self.bs8.build_battery()
        self.assertEqual('DNN0', b.form_factor)
        self.assertEqual('Lion', b.battery_type)
        self.assertEqual(7.8, b.storage_capacity)
        self.assertEqual(500, b.charge_cycles)
        self.assertEqual(10.12, b.price)

    def test_build_speakers(self):
        s = self.bs8.build_speakers()
        self.assertEqual('SpiffySoundTek', s.brand)
        self.assertEqual('28 - 22kHz', s.response_frequency)
        self.assertEqual(4, s.impedance)
        self.assertEqual(0.2, s.active_draw)
        self.assertEqual(0, s.passive_draw)
        self.assertEqual(5.00, s.price)

    def test_build_screen(self):
        s = self.bs8.build_screen()
        self.assertEqual(154.00, s.height)
        self.assertEqual(72.4, s.width)
        self.assertEqual(14, s.pixels_per_mm)
        self.assertEqual(round(s.height * s.pixels_per_mm), s.height_pixels)
        self.assertEqual(round(s.width * s.pixels_per_mm), s.width_pixels)
        self.assertEqual(60, s.refresh_rate)
        self.assertEqual(0.1, s.passive_draw)
        self.assertEqual(0.71, s.active_draw)
        self.assertEqual(55.69, s.price)

    def test_build_external_shell(self):
        es = self.bs8.build_external_shell()
        self.assertEqual('ABS', es.material)
        self.assertEqual(160, es.height)
        self.assertEqual(78, es.width)
        self.assertEqual(0.38, es.depth)
        self.assertEqual('1.2 ft.', es.drop_resistance_rating)
        self.assertEqual(8.10, es.assembly_cost)
        self.assertEqual(False, es.is_water_proof)
        self.assertEqual(True, es.is_dust_sand_proof)
        self.assertEqual(1.20, es.price)


if __name__ == "__main__":
    # execute only if run as a script
    unittest.main()
