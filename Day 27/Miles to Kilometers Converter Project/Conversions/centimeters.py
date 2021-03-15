class Centimeters:
    def __init__(self, val):
        self.val = val

    def convert_to_kilometer(self):
        return self.val / 100000

    def convert_to_meter(self):
        return self.val / 100

    def convert_to_centimeter(self):
        return self.val

    def convert_to_milimeter(self):
        return self.val * 10

    def convert_to_micrometer(self):
        return self.val * 10000

    def convert_to_nanometer(self):
        return self.val * 1e+7

    def convert_to_mile(self):
        return self.val / 160934

    def convert_to_yard(self):
        return self.val / 91.44

    def convert_to_foot(self):
        return self.val / 30.48

    def convert_to_inch(self):
        return self.val / 2.54

    def convert_to_nautical_mile(self):
        return self.val / 185200
