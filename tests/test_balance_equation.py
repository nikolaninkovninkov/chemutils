import sys
import os
import pytest
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from general_chemistry.balance_equation import balance_equation
from utils.create_dict_from_lists import create_dict_from_lists

def test_balance_equation():
    def test(reac_str, prod_str, coeff):
        reac_list = reac_str.split(' ')
        prod_list = prod_str.split(' ')
        coeff = [int(_) for _ in coeff.split(' ')]
        expected = (create_dict_from_lists(reac_list, coeff[0:len(reac_list)]), create_dict_from_lists(prod_list, coeff[len(reac_list):]))
        assert balance_equation(set(reac_list), set(prod_list)) == expected
    test("H2 O2", "H2O", "2 1 2")
    test("BrO3- H+ e-", "HBrO H2O", "1 5 4 1 2")
    test('CuS HNO3', 'Cu(NO3)2 S NO H2O', '3 8 3 3 2 4')
    test('NH4OH KAl(SO4)2(H2O)12', 'Al(OH)3 (NH4)2SO4 KOH H2O', '4 1 1 2 1 12')
    test('KNO3 C12H22O11', 'N2 CO2 H2O K2CO3', '48 5 24 36 55 24')
    test('O3 H2O e-', 'O2 OH-', '1 1 2 1 2')
    test('C O2', 'CO CO2', '3 2 2 1')
        