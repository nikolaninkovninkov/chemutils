import re
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from utils.fuckitonsteroids import fuckitonsteroids
from general_chemistry.Reaction import Reaction
@fuckitonsteroids("Basic equilibrium cannot be created")
def create_basic_equilibrium(form1, form2, K):
    return Reaction.create_balanced({'e-', form1}, {form2}, K)
    return Reaction.create_balanced({'e-', 'H2O', form1}, {'OH-', form2}, K)
    return Reaction.create_balanced({'e-', form1, 'H2O'}, {form2}, K)
    return Reaction.create_balanced({'e-', form1}, {form2, 'OH-'}, K)
    return Reaction.create_balanced({'e-', 'H2O', form1}, {'OH-'}, K)
    return None
