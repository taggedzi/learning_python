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


if __name__ == "__main__":
    # execute only if run as a script
    unittest.main()
