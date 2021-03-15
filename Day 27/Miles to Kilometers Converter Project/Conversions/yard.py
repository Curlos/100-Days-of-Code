class Yard:
    def __init__(self, val):
        self.val = val

    def convert_to_kilometer(self):
        return self.val / 1094

    def convert_to_meter(self):
        return self.val / 1.094

    def convert_to_centimeter(self):
        return self.val * 91.44

    def convert_to_milimeter(self):
        return self.val * 914

    def convert_to_micrometer(self):
        return self.val * 914400

    def convert_to_nanometer(self):
        return self.val * 9.144e+8

    def convert_to_mile(self):
        return self.val / 1760

    def convert_to_yard(self):
        return self.val

    def convert_to_foot(self):
        return self.val * 3

    def convert_to_inch(self):
        return self.val * 36

    def convert_to_nautical_mile(self):
        return self.val / 2025
