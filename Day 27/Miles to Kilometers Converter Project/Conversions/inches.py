class Inches:
    def __init__(self, val):
        self.val = val

    def convert_to_kilometer(self):
        return self.val / 39370

    def convert_to_meter(self):
        return self.val / 39.37

    def convert_to_centimeter(self):
        return self.val * 2.54

    def convert_to_milimeter(self):
        return self.val * 25.4

    def convert_to_micrometer(self):
        return self.val * 25400

    def convert_to_nanometer(self):
        return self.val * 2.54e+7

    def convert_to_mile(self):
        return self.val / 63360

    def convert_to_yard(self):
        return self.val / 36

    def convert_to_foot(self):
        return self.val / 12

    def convert_to_inch(self):
        return self.val / 39370

    def convert_to_nautical_mile(self):
        return self.val / 72913
