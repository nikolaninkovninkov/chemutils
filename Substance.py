from periodic_data import get_relative_molecular_mass


class Substance:
    def __init__(self, composition):
        self.composition = composition
    @property
    def mass(self):
        return get_relative_molecular_mass(self.composition)
    