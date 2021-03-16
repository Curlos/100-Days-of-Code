class Kilometers:
    def __init__(self, val):
        self.val = val

    def convert_to_kilometer(self):
        return self.val

    def convert_to_meter(self):
        return self.val * 1000

    def convert_to_centimeter(self):
        return self.val * 100000

    def convert_to_millimeter(self):
        return self.val * 1e+6

    def convert_to_micrometer(self):
        return self.val * 1e+9

    def convert_to_nanometer(self):
        return self.val * 1e+12

    def convert_to_mile(self):
        return self.val / 1.609

    def convert_to_yard(self):
        return self.val * 1094

    def convert_to_foot(self):
        return self.val * 3281

    def convert_to_inch(self):
        return self.val * 39370

    def convert_to_nautical_mile(self):
        return self.val / 1.852
