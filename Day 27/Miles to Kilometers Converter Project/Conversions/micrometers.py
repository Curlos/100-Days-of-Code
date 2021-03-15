class Micrometers:
    def __init__(self, val):
        self.val = val

    def convert_to_kilometer(self):
        return self.val / 1e+9

    def convert_to_meter(self):
        return self.val / 1e+6

    def convert_to_centimeter(self):
        return self.val / 10000

    def convert_to_milimeter(self):
        return self.val / 1000

    def convert_to_micrometer(self):
        return self.val

    def convert_to_nanometer(self):
        return self.val * 1000

    def convert_to_mile(self):
        return self.val / 1.609e+9

    def convert_to_yard(self):
        return self.val / 914400

    def convert_to_foot(self):
        return self.val / 304800

    def convert_to_inch(self):
        return self.val / 25400

    def convert_to_nautical_mile(self):
        return self.val / 1.852e+9
