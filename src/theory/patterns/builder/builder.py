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

Details about the Builder Pattern:
https://www.wikiwand.com/en/Builder_pattern

Details about the Property Decorator and Property Method:
https://docs.python.org/2/howto/descriptor.html#properties
"""


class CellPhone(object):
    """
    Product. This is the final product that is made up of components, that
    are built on the fly.
    """

    def __init__(self):
        self.__mfg = None
        self.__model = None
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

    @staticmethod
    def convert_seconds(seconds):
        """
        Given a number of seconds convert to days, hours, minutes, seconds
        :param seconds: Int  Number of seconds to calc
        :return: Tuple(days, hours, minutes, seconds)
        """
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        return days, hours, minutes, seconds

    @staticmethod
    def get_price(thing_to_price):
        """
        Get the price of a component.
        If one is not set or the component doesn't have one set the value to zero.
        :param thing_to_price: Object   Price
        :return: Int Price
        """
        answer = 0
        try:
            answer += thing_to_price.price
        except AttributeError as _:
            pass
        return answer

    @staticmethod
    def calculate_msrp(cost_price):
        """
        Return a msrp the actual cost multiplied by mark up of some kind.
        :param cost_price: Float  The cost of something
        :return: Float The price of something after markup.
        """
        return cost_price * 2.5

    @staticmethod
    def get_passive_current_draw(thing_to_calc):
        """
        Determine the passive electrical current draw of
        a component. If it has one.
        :param thing_to_calc: Object  A component object which may have a passive current draw
        :return:  Float  The current during passive draw of a component
        """
        current_draw = 0.0
        try:
            current_draw += thing_to_calc.passive_draw
        except AttributeError as _:
            pass
        return current_draw

    @staticmethod
    def get_active_current_draw(thing_to_calc):
        """
        Determine the active electrical current draw of a component.
        IF it has one.
        :param thing_to_calc: Object  A component object to check the draw of
        :return: Float the current draw of the object if it has one. If not 0.0
        """
        current_draw = 0.0
        try:
            current_draw += thing_to_calc.active_draw
        except AttributeError as _:
            pass
        return current_draw

    @staticmethod
    def convert_hours_to_seconds(milli_amp_hours):
        """
        Convert hours to seconds
        :param milli_amp_hours: Float Hours
        :return: Float seconds
        """
        return milli_amp_hours * 60 * 60

    @property
    def mfg(self):
        return self.__mfg

    @mfg.setter
    def mfg(self, manufacturer):
        self.__mfg = manufacturer

    @mfg.deleter
    def mfg(self):
        del self.__mfg

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @model.deleter
    def model(self):
        del self.__model

    @property
    def circuit_board(self):
        return self.__circuit_board

    @circuit_board.setter
    def circuit_board(self, circuit_board):
        self.__circuit_board = circuit_board

    @circuit_board.deleter
    def circuit_board(self):
        del self.__circuit_board

    @property
    def cellular_module(self):
        return self.__cellular_module

    @cellular_module.setter
    def cellular_module(self, module_type):
        self.__cellular_module = module_type

    @cellular_module.deleter
    def cellular_module(self):
        del self.__cellular_module

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, battery):
        self.__battery = battery

    @battery.deleter
    def battery(self):
        del self.__battery

    def get_speakers(self):
        return self.__speakers

    def set_speakers(self, speakers):
        self.__speakers = speakers

    def delete_speakers(self):
        del self.__speakers

    # Alternate syntax for property decorators
    speakers = property(get_speakers, set_speakers, delete_speakers)

    def get_screen(self):
        return self.__screen

    def set_screen(self, screen):
        self.__screen = screen

    def delete_screen(self):
        del self.__screen

    # Alternative syntax for property decorators
    screen = property(get_screen, set_screen, delete_screen)

    def get_external_shell(self):
        return self.__external_shell

    def set_external_shell(self, external_shell):
        self.__external_shell = external_shell

    def delete_external_shell(self):
        del self.__external_shell

    # Alternate property syntax
    external_shell = property(get_external_shell, set_external_shell, delete_external_shell)

    @property
    def total_price(self):
        total = self.get_price(self.circuit_board)
        total += self.get_price(self.cellular_module)
        total += self.get_price(self.battery)
        total += self.get_price(self.speakers)
        total += self.get_price(self.screen)
        total += self.get_price(self.external_shell)
        self.__price = total
        return total

    @property
    def assembled_price(self):
        assembly_cost = 0.0
        try:
            assembly_cost = self.external_shell.assembly_cost
        except AttributeError as _:
            pass
        return self.total_price + assembly_cost

    @property
    def passive_battery_duration(self):
        capacity = self.__battery.storage_capacity
        total_passive_draw = CellPhone.get_passive_current_draw(self.__circuit_board)
        total_passive_draw += CellPhone.get_passive_current_draw(self.__cellular_module)
        total_passive_draw += CellPhone.get_passive_current_draw(self.__speakers)
        total_passive_draw += CellPhone.get_passive_current_draw(self.__screen)
        milli_amp_seconds = CellPhone.convert_hours_to_seconds(capacity)
        self.__runtime_passive = self.convert_seconds(round(milli_amp_seconds / total_passive_draw))
        return self.__runtime_passive  # (days, hours, minutes, seconds)

    @property
    def active_battery_duration(self):
        capacity = self.__battery.storage_capacity
        total_active_draw = CellPhone.get_active_current_draw(self.__circuit_board)
        total_active_draw += CellPhone.get_active_current_draw(self.__cellular_module)
        total_active_draw += CellPhone.get_active_current_draw(self.__speakers)
        total_active_draw += CellPhone.get_active_current_draw(self.__screen)
        milli_amp_seconds = CellPhone.convert_hours_to_seconds(capacity)
        self.__runtime_active = self.convert_seconds(round(milli_amp_seconds / total_active_draw))
        return self.__runtime_active  # (days, hours, minutes, seconds)

    @property
    def brochure(self):
        output = "-" * 80 + "\n"
        output += "Manufacturer: {phone.mfg}; Model: {phone.model}\n".format(phone=self)
        output += "Primary board design: {board.model} v{board.revision}\n".format(board=self.circuit_board)
        output += "Supported cellular bands: {cell.bands}\n".format(cell=self.cellular_module)
        output += "Battery: Capacity: {battery.storage_capacity} mAH;\n" \
                  "\tEstimated standby time: {standby_time} days, hours, minutes, seconds;\n" \
                  "\tEstimated talk time: {talk_time} " \
                  "days, hours, minutes, seconds;\n".format(battery=self.battery,
                                                            standby_time=self.passive_battery_duration,
                                                            talk_time=self.active_battery_duration)
        output += "Speakers response frequency: {speakers.response_frequency}\n".format(speakers=self.speakers)
        output += "Screen resolution: {screen.width_pixels}x{screen.height_pixels} " \
                  "@ {screen.refresh_rate} hz\n".format(screen=self.screen)
        output += "External Dimensions: Height {shell.height} mm, Width {shell.width} mm, " \
                  "Depth {shell.depth} mm.\n".format(shell=self.external_shell)
        output += "MSRP: ${0:.2f};\n".format(self.calculate_msrp(self.total_price))
        return output

    def __str__(self):
        output = "Manufacturer: {self.mfg}; Model: {self.model};\n".format(self=self)
        output += str(self.circuit_board)
        output += str(self.cellular_module)
        output += str(self.battery)
        output += str(self.speakers)
        output += str(self.screen)
        output += str(self.external_shell)
        output += "Price of Parts: ${self.total_price:.2f} USD;\n".format(self=self)
        output += "Assembled Price: ${self.assembled_price:.2f} USD;\n".format(self=self)
        output += "Recommended MSRP: ${0:.2f} USD;\n".format(self.calculate_msrp(self.total_price))
        return output


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

    def __str__(self):
        output = "Circuit Board:\n"
        output += "\tModel: {self.model} v{self.revision}\n".format(self=self)
        output += "\tPower Consumption:\n"
        output += "\t\tMax: {self.active_draw} mA; Min {self.passive_draw} mA;\n".format(self=self)
        output += "\tPrice: ${self.price:.2f} USD\n".format(self=self)
        return output


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

    def __str__(self):
        output = "Cellular Module:\n"
        output += "\tManufacturer: {self.manufacturer}; Make: {self.make};\n".format(self=self)
        output += "\tSupported Cellular Protocols: {self.bands}\n".format(self=self)
        output += "\tPower Consumption:\n"
        output += "\t\tMax: {self.active_draw} mA; Min {self.passive_draw} mA;\n".format(self=self)
        output += "\tPrice: ${self.price:.2f} USD\n".format(self=self)
        return output


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

    def __str__(self):
        output = "Battery:\n"
        output += "\tForm factor: {self.form_factor}\n".format(self=self)
        output += "\tBattery type: {self.battery_type}\n".format(self=self)
        output += "\tStorage Capacity: {self.storage_capacity} mAh; " \
                  "Average Charging Cycles: {self.charge_cycles};\n".format(self=self)
        output += "\tPrice: ${self.price:.2f} USD;\n".format(self=self)
        return output


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

    def __str__(self):
        output = "Speakers:\n"
        output += "\tBrand: {self.brand}\n".format(self=self)
        output += "\tResponse Frequency: {self.response_frequency}\n".format(self=self)
        output += "\tElectrical Specs:\n"
        output += "\t\tImpedance: {self.impedance}\n".format(self=self)
        output += "\t\tMax Current Draw: {self.active_draw} mA; " \
                  "Min Current Draw: {self.passive_draw} mA\n".format(self=self)
        output += "\tPrice: ${self.price:.2f} USD\n".format(self=self)
        return output


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

    def __str__(self):
        output = "Screen:\n"
        output += "\tDimensions:\n"
        output += "\t\tHeight: {self.height} mm; Width: {self.width} mm\n".format(self=self)
        output += "\tDisplay Details:\n"
        output += "\t\tHeight in pixels: {self.height_pixels};\n".format(self=self)
        output += "\t\tWidth in pixels: {self.width_pixels};\n".format(self=self)
        output += "\t\tPixel Density (ppmm): {self.pixels_per_mm};\n".format(self=self)
        output += "\t\tRefresh Rate: {self.refresh_rate}\n".format(self=self)
        output += "\tCurrent Draw:\n"
        output += "\t\tMax Current Draw: {self.active_draw} mA; " \
                  "Min Current Draw: {self.passive_draw} mA\n".format(self=self)
        output += "\tPrice: ${self.price:.2f} USD\n".format(self=self)
        return output


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

    def __str__(self):
        output = "External Shell:\n"
        output += "\tConstruction Material: {self.material};\n".format(self=self)
        output += "\tDimensions:\n"
        output += "\t\tHeight: {self.height} mm; Width: {self.width} mm; Depth: {self.depth} mm;\n".format(self=self)
        output += "\tDrop Resistance: {self.drop_resistance_rating};\n".format(self=self)
        output += "\tWater Proof: {self.is_water_proof};\n".format(self=self)
        output += "\tDust and Sand Proof: {self.is_dust_sand_proof};\n".format(self=self)
        output += "\tPrice: ${self.price:.2f} USD;\n".format(self=self)
        output += "\tAssembly Cost: ${self.assembly_cost:.2f};\n".format(self=self)
        return output


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
        phone.circuit_board = self.__builder.build_circuit_board()
        phone.cellular_module = self.__builder.build_cellular_module()
        phone.battery = self.__builder.build_battery()
        phone.speakers = self.__builder.build_speakers()
        phone.screen = self.__builder.build_screen()
        phone.external_shell = self.__builder.build_external_shell()
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


# noinspection PyMethodMayBeStatic
class MeFone12(BuilderInterface):
    """
    Concrete Builder
    This is an exact configuration to assemble a specific instance of a cellphone.
    (aka the recipe required to make the MeFone 12)
    These methods could be FAR more complex to allow for the creation
    of all the variations of this type. However for this example I will
    just include the sub-classes with some mock data.
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


# noinspection PyMethodMayBeStatic
class BirdSungT8(BuilderInterface):
    """
    Concrete Builder
    This is an exact configuration to assemble a specific instance of a cellphone.
    (aka the recipe required to make the BirdSung T8)
    These methods could be FAR more complex to allow for the creation
    of all the variations of this type. However for this example I will
    just include the sub-classes with some mock data.
    """

    def __init__(self):
        self.mfg = "Birdsung"
        self.model = "T8"

    def build_circuit_board(self):
        return CircuitBoard('Cobalt', '2.0.4', .117, .021, 78.21)

    def build_cellular_module(self):
        return CellularModule('LuckySnaps', 'VINA99', ['3G', '4G', 'CDMA', 'FDMA', 'EVDO3'], .21, .008, 72.63)

    def build_battery(self):
        return Battery("DNN0", "Lion", 7.8, 500, 10.12)

    def build_speakers(self):
        return Speakers("SpiffySoundTek", "28 - 22kHz", 4, 0, .2, 5.00)

    def build_screen(self):
        return Screen(154.00, 72.4, 14, 60, 0.1, 0.71, 55.69)

    def build_external_shell(self):
        return ExternalShell('ABS', 160, 78, .38, '1.2 ft.', 8.10, False, True, 1.20)


def main():  # pragma: no cover
    d = Director()

    d.set_builder(MeFone12())
    me_phone_12 = d.build_phone()
    print(me_phone_12.brochure)
    print(me_phone_12)

    d.set_builder(BirdSungT8())
    bird_sung_t8 = d.build_phone()
    print(bird_sung_t8.brochure)
    print(bird_sung_t8)


if __name__ == "__main__":  # pragma: no cover
    # execute only if run as a script
    main()
