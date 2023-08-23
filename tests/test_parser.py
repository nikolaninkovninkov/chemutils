import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from utils.parsing import formula_to_composition
def test_formula_to_composition():
    assert formula_to_composition("H2O") == {1: 2, 8: 1}
    assert formula_to_composition("(SCN)2") == {16: 2, 6: 2, 7: 2}
    assert formula_to_composition("Ca(OH)2") == {20: 1, 8: 2, 1: 2}
    assert formula_to_composition("Na+") == {0: 1, 11: 1}
    assert formula_to_composition("[Cu(NH3)4(H2O)2]+2") == {29: 1, 7: 4, 1: 16, 8: 2, 0: 2}
    assert formula_to_composition("[CoCl4(NH3)2]-") == {27: 1, 17: 4, 7: 2, 1: 6, 0: -1}