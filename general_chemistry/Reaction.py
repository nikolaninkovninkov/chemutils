from typing import Dict, Set, Union

from general_chemistry.balance_equation import balance_equation
from utils.create_dict_from_lists import create_dict_from_lists
from general_chemistry.constants import constants
import math

from utils.create_dictionary_from_list import create_dictionary_from_list
class Reaction:
    def __init__(self, reactants:Dict[str, float], products: Dict[str, float], K: Union[float, None]):
        if set(reactants.keys()) & set(products.keys()):
            raise ValueError("Reaction cannot have the same compound in reactants and the products")
        self.reac = reactants
        self.prod = products
        self.K = K
    @classmethod
    def create_balanced(cls, reactants: Set[str], products: Set[str], K: Union[float, None]):
        if K:
            return Reaction(*balance_equation(reactants, products), K)
        return Reaction(*balance_equation(reactants, products))
    @property
    def reac_prod_combined(self):
        return {**{k: -v for k,v in self.reactants.items()}, **self.products}
    @property
    def z(self):
        if not 'e-' in self.reac_prod_combined:
            raise ValueError("Reaction must be a redox half reaction to get number of exchanged electrons")
        return abs(self.reac_prod_combined['e-'])
    @property
    def std_E(self, T=constants["std_T"]):
        if not 'e-' in self.reac_prod_combined:
            raise ValueError("Reaction must be a redox half reaction to get number of exchanged electrons")
        if not self.K:
            return None
        return constants['R']*T/(self.z*constants['F'])*math.log(self.K)
    def __str__(self):
        return_str = ''
        for i, (k,v) in enumerate(self.reac.items()):
            if i == len(self.reac.keys()) - 1:
                if v != 1:  
                    return_str += f'{v}{k}'
                else:
                    return_str += f'{k}'
            else:
                if v != 1:  
                    return_str += f'{v}{k} + '
                else:
                    return_str += f'{k} + '
        return_str += ' = '
        for i, (k,v) in enumerate(self.prod.items()):
            if i == len(self.prod.keys()) - 1:
                if v != 1:  
                    return_str += f'{v}{k}'
                else:
                    return_str += f'{k}'
            else:
                if v != 1:  
                    return_str += f'{v}{k} + '
                else:
                    return_str += f'{k} + '
        return return_str
