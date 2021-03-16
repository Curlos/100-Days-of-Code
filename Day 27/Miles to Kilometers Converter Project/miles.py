class Miles:
    def __init__(self, val):
        self.val = val

    def convert_to_kilometer(self):
        return self.val * 1.609

    def convert_to_meter(self):
        return self.val * 1609

    def convert_to_centimeter(self):
        return self.val * 160934

    def convert_to_millimeter(self):
        return self.val * 1.609e+6

    def convert_to_micrometer(self):
        return self.val * 1.609e+9

    def convert_to_nanometer(self):
        return self.val * 1.609e+12

    def convert_to_mile(self):
        return self.val

    def convert_to_yard(self):
        return self.val * 1760

    def convert_to_foot(self):
        return self.val * 5280

    def convert_to_inch(self):
        return self.val * 63360

    def convert_to_nautical_mile(self):
        return self.val / 1.151