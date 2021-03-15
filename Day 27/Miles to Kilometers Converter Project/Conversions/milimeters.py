class Millimeters:
    def __init__(self, val):
        self.val = val

    def convert_to_kilometer(self):
        return self.val / 1e+6

    def convert_to_meter(self):
        return self.val / 1000

    def convert_to_centimeter(self):
        return self.val / 10

    def convert_to_milimeter(self):
        return self.val

    def convert_to_micrometer(self):
        return self.val * 1000

    def convert_to_nanometer(self):
        return self.val * 1e+6

    def convert_to_mile(self):
        return self.val / 1.609e+6

    def convert_to_yard(self):
        return self.val / 914

    def convert_to_foot(self):
        return self.val / 305

    def convert_to_inch(self):
        return self.val / 25.4

    def convert_to_nautical_mile(self):
        return self.val / 1.852e+6
