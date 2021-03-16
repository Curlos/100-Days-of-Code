from kilometers import Kilometers
from meters import Meters
from centimeters import Centimeters
from millimeters import Millimeters
from micrometers import Micrometers
from nanometers import Nanometers
from miles import Miles
from yards import Yards
from feet import Feet
from inches import Inches
from nautical_miles import NauticalMiles

from pprint import pprint


class Converter():
    def __init__(self, val, unit):
        super().__init__()
        self.conversion_classes = {'kilometers': Kilometers(val),
                                   'meters': Meters(val),
                                   'centimeters': Centimeters(val),
                                   'millimeters': Millimeters(val),
                                   'micrometers': Micrometers(val),
                                   'nanometers': Nanometers(val),
                                   'miles': Miles(val),
                                   'yards': Yards(val),
                                   'feet': Feet(val),
                                   'inches': Inches(val),
                                   'nautical_miles': NauticalMiles(val)
                                   }
        self.unit = unit
        self.conversions = {}

    def convert(self):
        unit_class = self.conversion_classes[self.unit]
        self.conversions["kilometers"] = unit_class.convert_to_kilometer()
        self.conversions["meters"] = unit_class.convert_to_meter()
        self.conversions["centimeters"] = unit_class.convert_to_centimeter()
        self.conversions["millimeters"] = unit_class.convert_to_millimeter()
        self.conversions["micrometers"] = unit_class.convert_to_micrometer()
        self.conversions["nanometers"] = unit_class.convert_to_nanometer()
        self.conversions["miles"] = unit_class.convert_to_mile()
        self.conversions["yards"] = unit_class.convert_to_yard()
        self.conversions["feet"] = unit_class.convert_to_foot()
        self.conversions["inches"] = unit_class.convert_to_inch()
        self.conversions["nautical_miles"] = unit_class.convert_to_nautical_mile()

        return self.conversions


c = Converter(12, 'inches')
# return a dictionary of units as keys and converted calculation as values
pprint(c.convert())
