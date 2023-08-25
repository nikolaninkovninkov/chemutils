import re
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from utils.fuckitonsteroids import fuckitonsteroids
from general_chemistry.Reaction import Reaction
@fuckitonsteroids("Acidic equilibrium cannot be created")
def create_acidic_equilibrium(form1, form2, E = None):
    return Reaction.create_balanced_with_E({'e-', form1}, {form2}, E)
    return Reaction.create_balanced_with_E({'H+', 'e-', form1}, {form2}, E)
    return Reaction.create_balanced_with_E({'H+', 'e-', form1}, {'H2O', form2}, E)
    return Reaction.create_balanced_with_E({'H+', 'e-', form1, 'H2O'}, {form2}, E)
    return None