class Feet:
    def __init__(self, val):
        self.val = val

    def convert_to_kilometer(self):
        return self.val / 3281

    def convert_to_meter(self):
        return self.val / 3.281

    def convert_to_centimeter(self):
        return self.val * 30.48

    def convert_to_milimeter(self):
        return self.val * 305

    def convert_to_micrometer(self):
        return self.val * 304800

    def convert_to_nanometer(self):
        return self.val * 3.048e+8

    def convert_to_mile(self):
        return self.val / 5280

    def convert_to_yard(self):
        return self.val / 3

    def convert_to_foot(self):
        return self.val

    def convert_to_inch(self):
        return self.val * 12

    def convert_to_nautical_mile(self):
        return self.val / 6076
