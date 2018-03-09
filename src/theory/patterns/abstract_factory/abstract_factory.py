#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is an example of how a person could implement a basic
abstract factory pattern.  This is very similar to the factory pattern
but is abstracted one more layer.
"""


class MotorCycleInterface(object):
    """
    Abstract Motorcycle Class
    """

    def __init__(self):
        self.wheels = 2
        self.vehicle_type = "Motor Cycle"

    def set_model(self, model): pass

    def accelerate(self, speed): pass


class CarInterface(object):
    """
    Abstract Car Class
    """

    def __init__(self):
        self.wheels = 4
        self.vehicle_type = "Automobile"

    def set_model(self, model): pass

    def accelerate(self, speed): pass


class HarleyDavidson(MotorCycleInterface):
    """
    Concrete MotorCycle Class
    """

    def __init__(self):
        super(HarleyDavidson, self).__init__()
        self.mfg = "Harley Davidson"
        self.model = ""
        self.speed = 0

    def set_model(self, model):
        self.model = model

    def accelerate(self, speed):
        self.speed += speed


class Honda(MotorCycleInterface):
    """
    Concrete MotorCycle Class
    """

    def __init__(self):
        super(Honda, self).__init__()
        self.mfg = "Honda"
        self.model = ""
        self.speed = 0

    def set_model(self, model):
        self.model = model

    def accelerate(self, speed):
        self.speed += speed


class MercedezBenz(CarInterface):
    """
    Concrete Car Class
    """

    def __init__(self):
        super(MercedezBenz, self).__init__()
        self.mfg = "Mercedez-Benz"
        self.model = ""
        self.speed = 0

    def set_model(self, model):
        self.model = model

    def accelerate(self, speed):
        self.speed += speed


class Lexus(CarInterface):
    """
    Concrete Car Class
    """

    def __init__(self):
        super(Lexus, self).__init__()
        self.mfg = "Lexus"
        self.model = ""
        self.speed = 0

    def set_model(self, model):
        self.model = model

    def accelerate(self, speed):
        self.speed += speed


class VehicleFactoryInterface(object):
    """
    Abstract Factory Interface
    """

    def get_vehicle(self, brand): pass


class MotorCycleFactory(VehicleFactoryInterface):
    """
    Concrete Vehicle Factory
    """

    def get_vehicle(self, brand):
        if brand == "Harley Davidson":
            return HarleyDavidson()
        if brand == "Honda":
            return Honda()
        raise TypeError('Unknown brand specified.')


class CarFactory(VehicleFactoryInterface):
    """
    Concrete Vehicle Factory
    """

    def get_vehicle(self, brand):
        if brand == "Mercedez-Benz":
            return MercedezBenz()
        if brand == "Lexus":
            return Lexus()
        raise TypeError('Unknown brand specified.')


def print_vehicle_specs(vehicle):
    """
    This function takes a vehicle defined above and prints out
    its details. We can do this because of duck typing. All of the
    vehicles defined above have the parameters and methods required to
    perform the actions.
    :param vehicle:
    :return:
    """
    print("This vehicle is a: {0.vehicle_type} and has {0.wheels} wheels.".format(vehicle))
    print("This vehicle is a {0.mfg} - {0.model} with a speed of {0.speed}".format(vehicle))
    print()


def set_vehicle_properties(type_, make, model, speed):
    """
    This function takes the basic attributes of a request and calls
    the correct factory, then sets any other attributes on the vehicle
    once it has been returned from the factory.
    :param type_:  STR  Type of vehicle
    :param make:   STR  Manufacturer Name
    :param model:  STR  Vehicle model Name
    :param speed:  INT  An integer indicating relative speed
    :return:  vehicle_class
    """
    if type_ == "Motorcycle":
        vehicle_factory = MotorCycleFactory()
    elif type_ == "Automobile":
        vehicle_factory = CarFactory()
    else:
        raise TypeError('You must specify a Motorcycle or an Automobile for type.')

    # we can do this because all of the factories implement
    # the abstract class VehicleInterface So we know that they will have the required
    # Methods available. Like get_vehicle()
    v = vehicle_factory.get_vehicle(make)

    # We can do these two lines because all of the vehicles we generate
    # implement the abstract class CarInterface OR MotorcycleInterface
    # and they both require that the set_model and accelerate methods be created.
    # This would be an example of duck typing.
    v.set_model(model)
    v.accelerate(speed)
    return v


def main():
    """
    This method creates 4 vehicles and prints out their information
    :return:
    """
    harley = set_vehicle_properties("Motorcycle", "Harley Davidson", "Touring", 100)
    honda = set_vehicle_properties("Motorcycle", "Honda", "CBR125R", 125)
    mercedez = set_vehicle_properties("Automobile", "Mercedez-Benz", "Mercedes-AMG C 63 Sedan", 95)
    lexus = set_vehicle_properties("Automobile", "Lexus", "RX 350", 85)

    print_vehicle_specs(harley)
    print_vehicle_specs(honda)
    print_vehicle_specs(mercedez)
    print_vehicle_specs(lexus)


if __name__ == "__main__":  # pragma: no cover
    # execute only if run as a script
    main()
