from typing import Dict, Set, Union

from general_chemistry.balance_equation import balance_equation
from utils.create_dict_from_lists import create_dict_from_lists
from general_chemistry.constants import constants
import math

from utils.create_dictionary_from_list import create_dictionary_from_list
class Reaction:
    def __init__(self, reactants:Dict[str, float], products: Dict[str, float], K: Union[float, None]=None):
        if set(reactants.keys()) & set(products.keys()):
            raise ValueError("Reaction cannot have the same compound in reactants and the products")
        self.reac = reactants
        self.prod = products
        self.K = K
    @classmethod
    def create_balanced(cls, reactants: Set[str], products: Set[str], K: Union[float, None]=None):
        if K:
            return Reaction(*balance_equation(reactants, products), K)
        return Reaction(*balance_equation(reactants, products))
    @classmethod
    def create_balanced_with_E(cls, reactants: Set[str], products: Set[str], E: Union[float, None]=None, T=constants["std_T"]):
        rxn =  Reaction(*balance_equation(reactants, products))
        if E:
            return Reaction(rxn.reac, rxn.prod, math.exp(rxn.z*constants['F']*E/constants['R']/T))
        return Reaction(rxn.reac, rxn.prod)
    @property
    def reac_prod_combined(self):
        return {**{k: -v for k,v in self.reac.items()}, **self.prod}
    @property
    def z(self):
        if not 'e-' in self.reac_prod_combined:
            raise ValueError("Reaction must be a redox half reaction to get number of exchanged electrons")
        return abs(self.reac_prod_combined['e-'])
    @property
    def std_E(self):
        if not 'e-' in self.reac_prod_combined:
            raise ValueError("Reaction must be a redox half reaction to get number of exchanged electrons")
        if not self.K:
            return None
        return constants['R']*constants['std_T']/(self.z*constants['F'])*math.log(self.K)
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
    def __mul__(self, other):
        if not isinstance(other, (float, int)):
            raise TypeError("Multiplication cannot be completed with an object that is not a number")
        flip = False
        if other < 0:
            other = abs(other)
            flip = True
        other = float(other)
        new_reac = {k: v*other for k,v in self.reac.items()}
        new_prod = {k: v*other for k,v in self.prod.items()}
        if flip:
            new_reac, new_prod = new_prod, new_reac
        if self.K:
            return Reaction(new_reac, new_prod, self.K**other)
        return Reaction(new_reac, new_prod)
    def __add__(self, other):
        if not isinstance(other, Reaction):
            raise TypeError("Addition of a reaction can only be performed with another reaction")
        new_reac_prod_combined = self.reac_prod_combined.copy()
        for k, v in other.reac_prod_combined.items():
            if k in new_reac_prod_combined:
                new_reac_prod_combined[k] += v
            else:
                new_reac_prod_combined[k] = v
        new_reac = {k: -v for k, v in new_reac_prod_combined if v < 0}
        new_prod = {k: v for k, v in new_reac_prod_combined if v > 0}
        if self.K and other.K:
            return Reaction(new_reac, new_prod, self.K*other.K)
        return Reaction(new_reac, new_prod)            
    def __neg__(self):
        return -1*self
    def __sub__(self, other):
        return self + -1 * other
    def __rmul__(self, other):
        return other * self