class Nanometers:
    def __init__(self, val):
        self.val = val

    def convert_to_kilometer(self):
        return self.val / 1e+12

    def convert_to_meter(self):
        return self.val / 1e+9

    def convert_to_centimeter(self):
        return self.val / 1e+7

    def convert_to_milimeter(self):
        return self.val / 1e+6

    def convert_to_micrometer(self):
        return self.val / 1000

    def convert_to_nanometer(self):
        return self.val

    def convert_to_mile(self):
        return self.val / 1.609e+12

    def convert_to_yard(self):
        return self.val / 9.144e+8

    def convert_to_foot(self):
        return self.val / 3.048e+8

    def convert_to_inch(self):
        return self.val / 2.54e+7

    def convert_to_nautical_mile(self):
        return self.val / 1.852e+12
