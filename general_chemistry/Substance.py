from general_chemistry.periodic_data import get_relative_molecular_mass
from utils.parsing import formula_to_composition


class Substance:
    def __init__(self, composition):
        self.composition = composition
    @property
    def mass(self):
        return get_relative_molecular_mass(self.composition)
    @classmethod
    def from_formula(cls, formula):
        composition = formula_to_composition(formula)
        return Substance(composition)