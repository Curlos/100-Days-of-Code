class NauticalMiles:
    def __init__(self, val):
        self.val = val

    def convert_to_kilometer(self):
        return self.val * 1.852

    def convert_to_meter(self):
        return self.val * 1852

    def convert_to_centimeter(self):
        return self.val * 185200

    def convert_to_millimeter(self):
        return self.val * 1.852e+6

    def convert_to_micrometer(self):
        return self.val * 1.852e+9

    def convert_to_nanometer(self):
        return self.val * 1.852e+12

    def convert_to_mile(self):
        return self.val * 1.151

    def convert_to_yard(self):
        return self.val * 2025

    def convert_to_foot(self):
        return self.val * 6076

    def convert_to_inch(self):
        return self.val * 72913

    def convert_to_nautical_mile(self):
        return self.val
