import re
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from utils.fuckitonsteroids import fuckitonsteroids
from general_chemistry.Reaction import Reaction
@fuckitonsteroids("Basic equilibrium cannot be created")
def create_basic_equilibrium(form1, form2, E):
    return Reaction.create_balanced_with_E({'e-', form1}, {form2}, E)
    return Reaction.create_balanced_with_E({'e-', 'H2O', form1}, {'OH-', form2}, E)
    return Reaction.create_balanced_with_E({'e-', form1, 'H2O'}, {form2}, E)
    return Reaction.create_balanced_with_E({'e-', form1}, {form2, 'OH-'}, E)
    return Reaction.create_balanced_with_E({'e-', 'H2O', form1}, {'OH-'}, E)
    return None
