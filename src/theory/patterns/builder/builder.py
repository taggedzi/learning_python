#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is a sample of a builder pattern.
You have an object that is made up of other smaller components, that
are constructed by a director. The director calls a builder which knows
knows how to assemble the objects and the and return them to the director.
This allows you to have the client code know nothing about how to construct
the objects but get complex and intricate objects that vary at build time.
it also allows loose coupling between client and object construction.
"""


class CellPhone(object):
    """
    Product. This is the final product that is made up of components, that
    are built on the fly.
    """
    def __init__(self):
        self.mgf = None
        self.model = None
        self.__cellular_module = None
        self.__circuit_board = None
        self.__revision = None
        self.__battery = None
        self.__speakers = None
        self.__screen = None
        self.__external_shell = None
        self.__price = None
        self.__passive_battery_life = None
        self.__active_battery_life = None
        self.__runtime_passive = None
        self.__runtime_active = None

    def add_circuit_board(self, circuit_board):
        self.__circuit_board = circuit_board

    def add_cellular_module(self, module_type):
        self.__cellular_module = module_type

    def add_battery(self, battery):
        self.__battery = battery

    def add_speakers(self, speakers):
        self.__speakers = speakers

    def add_screen(self, screen):
        self.__screen = screen

    def add_external_shell(self, external_shell):
        self.__external_shell = external_shell

    @staticmethod
    def convert_seconds(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        return days, hours, minutes, seconds

    @staticmethod
    def get_price(thing_to_price):
        answer = 0
        try:
            answer += thing_to_price.price
        except AttributeError as _:
            pass
        return answer

    @staticmethod
    def calculate_msrp(cost_price):
        return cost_price * 2.5

    @staticmethod
    def get_passive_current_draw(thing_to_calc):
        current_draw = 0
        try:
            current_draw += thing_to_calc.passive_draw
        except AttributeError as _:
            pass
        return current_draw

    @staticmethod
    def get_active_current_draw(thing_to_calc):
        current_draw = 0
        try:
            current_draw += thing_to_calc.active_draw
        except AttributeError as _:
            pass
        return current_draw

    @staticmethod
    def convert_hours_to_seconds(milli_amp_hours):
        return milli_amp_hours * 60 * 60

    def calculate_total_price(self):
        total = self.get_price(self.__circuit_board)
        total += self.get_price(self.__cellular_module)
        total += self.get_price(self.__battery)
        total += self.get_price(self.__speakers)
        total += self.get_price(self.__screen)
        total += self.get_price(self.__external_shell)
        self.__price = total
        return total

    def calculate_passive_battery_time(self):
        capacity = self.__battery.storage_capacity
        total_passive_draw = CellPhone.get_passive_current_draw(self.__circuit_board)
        total_passive_draw += CellPhone.get_passive_current_draw(self.__cellular_module)
        total_passive_draw += CellPhone.get_passive_current_draw(self.__speakers)
        total_passive_draw += CellPhone.get_passive_current_draw(self.__screen)
        milli_amp_seconds = CellPhone.convert_hours_to_seconds(capacity)
        self.__runtime_passive = self.convert_seconds(round(milli_amp_seconds / total_passive_draw))
        return self.__runtime_passive  # In seconds

    def calculate_active_battery_time(self):
        capacity = self.__battery.storage_capacity
        total_active_draw = CellPhone.get_active_current_draw(self.__circuit_board)
        total_active_draw += CellPhone.get_active_current_draw(self.__cellular_module)
        total_active_draw += CellPhone.get_active_current_draw(self.__speakers)
        total_active_draw += CellPhone.get_active_current_draw(self.__screen)
        milli_amp_seconds = CellPhone.convert_hours_to_seconds(capacity)
        self.__runtime_active = self.convert_seconds(round(milli_amp_seconds / total_active_draw))
        return self.__runtime_active  # In seconds

    def specification(self):
        print("-" * 80)
        print("Manufacturer: {phone.mfg}; Model: {phone.model}".format(phone=self))
        print("Primary board design: {board.model} v{board.revision}".format(board=self.__circuit_board))
        print("Supported cellular bands: {cell.bands}".format(cell=self.__cellular_module))
        print(
            "Battery: Capacity: {battery.storage_capacity} mAH; \n"
            "\tEstimated standby time: {standby_time} days, hours, minutes, seconds; \n"
            "\tEstimated talk time: {talk_time} days, hours, minutes, seconds".format(
                battery=self.__battery, standby_time=self.calculate_passive_battery_time(),
                talk_time=self.calculate_active_battery_time()))
        print("Speakers response frequency: {speakers.response_frequency}".format(speakers=self.__speakers))
        print("Screen resolution: {screen.width_pixels}x{screen.height_pixels} "
              "@ {screen.refresh_rate} hz".format(screen=self.__screen))
        print("External Dimensions: Height {shell.height} mm, Width {shell.width} mm, "
              "Depth {shell.depth} mm.".format(shell=self.__external_shell))
        print("Build Price: ${0:.2f}; MSRP: ${1:.2f};".format(self.calculate_total_price(),
                                                              self.calculate_msrp(self.calculate_total_price())))


class CircuitBoard(object):
    """
    Sub-component of a product highly configurable
    """
    def __init__(self, model, revision, active_current_draw, passive_current_draw, price):
        self.model = model
        self.revision = revision
        self.active_draw = active_current_draw
        self.passive_draw = passive_current_draw
        self.price = price


class CellularModule(object):
    """
    Sub-component of a product highly configurable
    """
    def __init__(self, manufacturer, make, bands, active_current_draw, passive_current_draw, price):
        self.manufacturer = manufacturer
        self.make = make
        self.bands = bands
        self.active_draw = active_current_draw
        self.passive_draw = passive_current_draw
        self.price = price


class Battery(object):
    """
    Sub-component of a product highly configurable
    """
    def __init__(self, form_factor, battery_type, storage_capacity, charge_cycles, price):
        self.form_factor = form_factor
        self.battery_type = battery_type
        self.storage_capacity = storage_capacity
        self.charge_cycles = charge_cycles
        self.price = price


class Speakers(object):
    """
    Sub-component of a product highly configurable
    """
    def __init__(self, brand, response_frequency, impedance, passive_current_draw, active_current_draw, price):
        self.brand = brand
        self.response_frequency = response_frequency
        self.impedance = impedance
        self.passive_draw = passive_current_draw
        self.active_draw = active_current_draw
        self.price = price


class Screen(object):
    """
    Sub-component of a product highly configurable
    """
    def __init__(self, height_mm, width_mm, pixels_per_mm, refresh_rate, passive_current_draw, active_current_draw,
                 price):
        self.height = height_mm
        self.width = width_mm
        self.pixels_per_mm = pixels_per_mm
        self.height_pixels = round(self.height * self.pixels_per_mm)
        self.width_pixels = round(self.width * self.pixels_per_mm)
        self.refresh_rate = refresh_rate
        self.passive_draw = passive_current_draw
        self.active_draw = active_current_draw
        self.price = price


class ExternalShell(object):
    """
    Sub-component of a product highly configurable
    """
    def __init__(self, material, height, width, depth, drop_resistance_rating, assembly_cost_per_unit, is_water_proof,
                 is_dust_sand_proof, price):
        self.material = material
        self.height = height
        self.width = width
        self.depth = depth
        self.drop_resistance_rating = drop_resistance_rating
        self.assembly_cost = assembly_cost_per_unit
        self.is_water_proof = is_water_proof
        self.is_dust_sand_proof = is_dust_sand_proof
        self.price = price


class Director(object):
    """
    This is the director class. The director has the __builder
    set to the concrete product builder. Then the Director
    calls the builder to assemble the exactly specified product
    """
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def build_phone(self):
        phone = CellPhone()

        phone.mfg = self.__builder.mfg
        phone.model = self.__builder.model

        circuit_board = self.__builder.build_circuit_board()
        phone.add_circuit_board(circuit_board)

        cellular_module = self.__builder.build_cellular_module()
        phone.add_cellular_module(cellular_module)

        battery = self.__builder.build_battery()
        phone.add_battery(battery)

        speakers = self.__builder.build_speakers()
        phone.add_speakers(speakers)

        screen = self.__builder.build_screen()
        phone.add_screen(screen)

        external_shell = self.__builder.build_external_shell()
        phone.add_external_shell(external_shell)

        return phone


class BuilderInterface(object):
    """
    Builder Interface, can be skipped, but it keeps all of the
    concrete builders in line and ensures the concrete builders
    still have the methods required.
    """
    def build_circuit_board(self): pass

    def build_cellular_module(self): pass

    def build_battery_module(self): pass

    def build_speakers(self): pass

    def build_screen(self): pass

    def build_external_shell(self): pass


class MeFone12(BuilderInterface):
    """
    Concrete Builder
    This is an exact configuration to assemble a specific instance of a cellphone.
    """
    def __init__(self):
        self.mfg = "NBD"
        self.model = "MeFone12"

    def build_circuit_board(self):
        return CircuitBoard('MRL-0032', '1.3.7a', .127, .018, 98.79)

    def build_cellular_module(self):
        return CellularModule('Kellog', 'ARNIL-3', ['3G', '4G', 'LTE'], .118, .006, 75.33)

    def build_battery(self):
        return Battery("M-004", "NiCAD", 8, 250, 5.38)

    def build_speakers(self):
        return Speakers("Lanteek", "35 - 21 kHz", 4, 0, .2, 5.00)

    def build_screen(self):
        return Screen(158.4, 78.1, 17.78, 60, 0.3, 0.68, 65.88)

    def build_external_shell(self):
        return ExternalShell('Aluminum', 158.9, 85.1, .4, '3 ft.', 12.10, False, False, 6.12)


class BirdSungT8(BuilderInterface):
    """
    Concrete Builder
    This is an exact configuration to assemble a specific instance of a cellphone.
    """
    def __init__(self):
        self.mfg = "Birdsung"
        self.model = "T8"

    def build_circuit_board(self):
        return CircuitBoard('Cobalt', '2.0.4', .117, .021, 78.21)

    def build_cellular_module(self):
        return CellularModule('LukySnaps', 'VINA99', ['3G', '4G', 'CDMA', 'FDMA', 'EVDO3'], .21, .008, 72.63)

    def build_battery(self):
        return Battery("DNN0", "Lion", 7.8, 500, 10.12)

    def build_speakers(self):
        return Speakers("SpiffySoundTek", "28 - 22kHz", 4, 0, .2, 5.00)

    def build_screen(self):
        return Screen(154.00, 72.4, 14, 60, 0.1, 0.71, 55.69)

    def build_external_shell(self):
        return ExternalShell('ABS', 160, 78, .38, '1.2 ft.', 8.10, False, True, 1.20)


def main():
    d = Director()

    d.set_builder(MeFone12())
    me_phone_12 = d.build_phone()
    me_phone_12.specification()

    d.set_builder(BirdSungT8())
    bird_sung_t8 = d.build_phone()
    bird_sung_t8.specification()


if __name__ == "__main__":
    # execute only if run as a script
    main()
