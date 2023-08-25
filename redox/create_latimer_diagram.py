import re
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from redox.create_acidic_equilibrium import create_acidic_equilibrium
from redox.create_basic_equilibrium import create_basic_equilibrium
from typing import Union

def create_latimer_diagram(forms: str, type: str, EPs:Union[str, None]  = None):
    if type == 'acidic':
        pass
    elif type == 'basic':
        pass
    else:
        raise ValueError('Type must be basic or acidic')
    forms_list = forms.split('=')
    reaction_pairs = []
    for i, form in enumerate(forms_list[:-1]):
        reaction_pairs.append((form, forms_list[i+1]))
    if EPs and len(EPs) != len(reaction_pairs):
        raise ValueError('Each reaction pair must have a corresponding equilibrium constant')
    reactions = []
    create_eq_func = create_acidic_equilibrium if type == 'acidic' else create_basic_equilibrium
    for i, reaction_pair in enumerate(reaction_pairs):
        reactions.append(create_eq_func(*reaction_pair, EPs[i] if EPs else None))
    return reactions
# rxns2 = create_latimer_diagram('SO4-2=SO3-2=S2O3-2=S=HS-', 'basic', [1, 2, 3, 4])
# print('-----')
# [print(_) for _ in rxns2]
rxns1 = create_latimer_diagram('H3PO4=H4P2O6=H3PO3=H3PO2=P=PH3', 'acidic')
[print(_) for _ in rxns1]
