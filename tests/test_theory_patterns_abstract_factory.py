#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from unittest.mock import Mock, patch, call
from src.theory.patterns.abstract_factory.abstract_factory import MotorCycleInterface
from src.theory.patterns.abstract_factory.abstract_factory import CarInterface
from src.theory.patterns.abstract_factory.abstract_factory import HarleyDavidson
from src.theory.patterns.abstract_factory.abstract_factory import Honda
from src.theory.patterns.abstract_factory.abstract_factory import MercedezBenz
from src.theory.patterns.abstract_factory.abstract_factory import Lexus
from src.theory.patterns.abstract_factory.abstract_factory import VehicleFactoryInterface
from src.theory.patterns.abstract_factory.abstract_factory import MotorCycleFactory
from src.theory.patterns.abstract_factory.abstract_factory import CarFactory
from src.theory.patterns.abstract_factory.abstract_factory import print_vehicle_specs
from src.theory.patterns.abstract_factory.abstract_factory import set_vehicle_properties
from src.theory.patterns.abstract_factory.abstract_factory import main as af_main


class TestMotorCycleInterface(unittest.TestCase):

    def test_motor_cycle_interface(self):
        mci = MotorCycleInterface()
        self.assertEqual(2, mci.wheels)
        self.assertEqual("Motor Cycle", mci.vehicle_type)


class TestCarInterface(unittest.TestCase):

    def test_car_interface(self):
        ci = CarInterface()
        self.assertEqual(4, ci.wheels)
        self.assertEqual("Automobile", ci.vehicle_type)


class TestHarleyDavidson(unittest.TestCase):

    def test_vehicle(self):
        v = HarleyDavidson()
        self.assertEqual("Harley Davidson", v.mfg)
        self.assertEqual(0, v.speed)

    def test_set_model(self):
        v = HarleyDavidson()
        v.set_model("test1")
        self.assertEqual("test1", v.model)

    def test_accelerate(self):
        v = HarleyDavidson()
        v.accelerate(100)
        self.assertEqual(100, v.speed)


class TestHonda(unittest.TestCase):

    def test_vehicle(self):
        v = Honda()
        self.assertEqual("Honda", v.mfg)
        self.assertEqual(0, v.speed)

    def test_set_model(self):
        v = Honda()
        v.set_model("test1")
        self.assertEqual("test1", v.model)

    def test_accelerate(self):
        v = Honda()
        v.accelerate(100)
        self.assertEqual(100, v.speed)


class TestMercedezBenz(unittest.TestCase):

    def test_vehicle(self):
        v = MercedezBenz()
        self.assertEqual("Mercedez-Benz", v.mfg)
        self.assertEqual(0, v.speed)

    def test_set_model(self):
        v = MercedezBenz()
        v.set_model("test1")
        self.assertEqual("test1", v.model)

    def test_accelerate(self):
        v = MercedezBenz()
        v.accelerate(100)
        self.assertEqual(100, v.speed)


class TestLexus(unittest.TestCase):

    def test_vehicle(self):
        v = Lexus()
        self.assertEqual("Lexus", v.mfg)
        self.assertEqual(0, v.speed)

    def test_set_model(self):
        v = Lexus()
        v.set_model("test1")
        self.assertEqual("test1", v.model)

    def test_accelerate(self):
        v = Lexus()
        v.accelerate(100)
        self.assertEqual(100, v.speed)


class TestVehicleFactoryInterface(unittest.TestCase):

    def test_vehicle_factory_interface(self):
        f = VehicleFactoryInterface()
        self.assertTrue(type(f) is VehicleFactoryInterface)


class TestMotorCycleFactory(unittest.TestCase):

    def test_motor_cycle_factory_harley_pass(self):
        f = MotorCycleFactory()
        result = f.get_vehicle('Harley Davidson')
        self.assertTrue(type(result) is HarleyDavidson)
        self.assertTrue(result.__class__.__base__.__name__ is "MotorCycleInterface")
        self.assertTrue(result.__class__.__base__.__base__.__name__ == "object")

    def test_motor_cycle_factory_honda_pass(self):
        f = MotorCycleFactory()
        result = f.get_vehicle('Honda')
        self.assertTrue(type(result) is Honda)
        self.assertTrue(result.__class__.__base__.__name__ is "MotorCycleInterface")
        self.assertTrue(result.__class__.__base__.__base__.__name__ == "object")

    def test_motor_cycle_factory_bogus_exception_thrown(self):
        f = MotorCycleFactory()
        with self.assertRaises(TypeError) as context:
            f.get_vehicle('Bogus')
        self.assertTrue("Unknown brand specified." in context.exception.args[0])


class TestCarFactory(unittest.TestCase):

    def test_car_factory_mercedez_pass(self):
        f = CarFactory()
        result = f.get_vehicle('Mercedez-Benz')
        self.assertTrue(type(result) is MercedezBenz)
        self.assertTrue(result.__class__.__base__.__name__ is "CarInterface")
        self.assertTrue(result.__class__.__base__.__base__.__name__ == "object")

    def test_car_factory_lexus_pass(self):
        f = CarFactory()
        result = f.get_vehicle('Lexus')
        self.assertTrue(type(result) is Lexus)
        self.assertTrue(result.__class__.__base__.__name__ is "CarInterface")
        self.assertTrue(result.__class__.__base__.__base__.__name__ == "object")

    def test_car_factory_bogus_exception_thrown(self):
        f = CarFactory()
        with self.assertRaises(TypeError) as context:
            f.get_vehicle('Bogus')
        self.assertTrue("Unknown brand specified." in context.exception.args[0])


class TestAbstractFactoryFunctions(unittest.TestCase):

    @patch('sys.stdout')
    def test_print_vehicle_specs(self, mock_print):
        f = CarFactory()
        result = f.get_vehicle('Lexus')
        result.set_model("test_model")
        result.accelerate(10)
        print_vehicle_specs(result)

        expected = [call.write('This vehicle is a: Automobile and has 4 wheels.'),
                    call.write('This vehicle is a Lexus - test_model with a speed of 10')]
        mock_print.assert_has_calls(expected, any_order=True)

    def assert_property_properly_set(self, vehicle, expected_class, expected_type, expected_wheels, expected_mfg,
                                     expected_model, expected_speed):
        self.assertTrue(type(vehicle) is expected_class)
        self.assertEqual(expected_type, vehicle.vehicle_type)
        self.assertEqual(expected_mfg, vehicle.mfg)
        self.assertEqual(expected_model, vehicle.model)
        self.assertTrue(expected_speed, vehicle.speed)
        self.assertTrue(expected_wheels, vehicle.wheels)

    """
    The following tests are more like functional tests than unit test but sometimes
    this is not a bad thing. If you wanted to make this more of a true unit test
    you would mock the factory classes and see if they are called with the right params
    then you would just be ensuring that the method being tested calls what it is supposed 
    to and trust that the methods it calls (which should be unit tested) will behave as expected.
    """
    def test_vehicle_properties_harley(self):
        v = set_vehicle_properties("Motorcycle", "Harley Davidson", "test harley", 17)
        self.assert_property_properly_set(v, HarleyDavidson, "Motor Cycle", 2, "Harley Davidson", "test harley", 17)

    def test_vehicle_properties_honda(self):
        v = set_vehicle_properties("Motorcycle", "Honda", "test honda", 18)
        self.assert_property_properly_set(v, Honda, "Motor Cycle", 2, "Honda", "test honda", 18)

    def test_vehicle_properties_mercedez(self):
        v = set_vehicle_properties("Automobile", "Mercedez-Benz", "test mercedez", 19)
        self.assert_property_properly_set(v, MercedezBenz, "Automobile", 4, "Mercedez-Benz", "test mercedez", 19)

    def test_vehicle_properties_lexus(self):
        v = set_vehicle_properties("Automobile", "Lexus", "test lexus", 20)
        self.assert_property_properly_set(v, Lexus, "Automobile", 4, "Lexus", "test lexus", 20)

    def test_vehicle_properties_bad_type_exception(self):
        with self.assertRaises(TypeError) as context:
            set_vehicle_properties("Bat mobile", "Wayne Enterprises", "Tumbler ", 99)
        self.assertEqual('You must specify a Motorcycle or an Automobile for type.', context.exception.args[0])

    @patch('src.theory.patterns.abstract_factory.abstract_factory.set_vehicle_properties')
    @patch('src.theory.patterns.abstract_factory.abstract_factory.print_vehicle_specs')
    def test_main(self, mock_print, mock_vehicle):
        mock_vehicle.return_value = Mock()
        af_main()
        expected_vehicle_calls = [call('Motorcycle', 'Harley Davidson', 'Touring', 100),
                                  call('Motorcycle', 'Honda', 'CBR125R', 125),
                                  call('Automobile', 'Mercedez-Benz', 'Mercedes-AMG C 63 Sedan', 95),
                                  call('Automobile', 'Lexus', 'RX 350', 85)]
        mock_vehicle.assert_has_calls(expected_vehicle_calls)
        self.assertEqual(4, mock_print.call_count)


if __name__ == "__main__":
    # execute only if run as a script
    unittest.main()
