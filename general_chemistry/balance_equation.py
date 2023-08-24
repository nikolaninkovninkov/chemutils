from typing import Set
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from utils.solve_chemical_matrix import solve_matrix
from utils.parsing import formula_to_composition
from utils.create_dict_from_lists import create_dict_from_lists
from sympy import Matrix, lcm
def balance_equation(reac: Set[str], prod: Set[str]):
    if set(reac) & set(prod):
        raise ValueError("Duplicates in reactants and products")
    reaclist = list(reac)
    prodlist = list(prod)
    reac_compositions = [formula_to_composition(_) for _ in reaclist]
    prod_compositions = [formula_to_composition(_) for _ in prodlist]
    unique_elements_reac = set().union(*[set(_.keys()) for _ in reac_compositions])
    unique_elements_prod = set().union(*[set(_.keys()) for _ in prod_compositions])
    if set(x for x in unique_elements_reac if x != 0) != set(x for x in unique_elements_prod if x != 0):
        raise ValueError("Equation cannot be balanced. Elements are different in reac and prod")
    sorted_unique_elements = sorted(list(unique_elements_reac))
    vertical_matrix_lines = []
    for reac_composition in reac_compositions:
        vertical_matrix_lines.append([reac_composition.get(_, 0) for _ in sorted_unique_elements])
    for prod_composition in prod_compositions:
        vertical_matrix_lines.append([-prod_composition.get(_, 0) for _ in sorted_unique_elements])
    matrix = [list(_) for _ in list(zip(*vertical_matrix_lines))]
    # print(matrix)
    # for row in matrix:
    #     print(' '.join([str(_) for _ in row]))
    coeff = solve_matrix(matrix)
    reac_coeff = create_dict_from_lists(reaclist, coeff[0:len(reaclist)])
    prod_coeff = create_dict_from_lists([*prodlist], coeff[len(reaclist):])
    reac_coeff = {k: v for k, v in reac_coeff.items() if v != 0}
    prod_coeff = {k: v for k, v in prod_coeff.items() if v != 0}
    return reac_coeff, prod_coeff