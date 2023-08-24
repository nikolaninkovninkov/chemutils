import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from general_chemistry.balance_equation import balance_equation
from general_chemistry.Reaction import Reaction
from redox.create_basic_equilibrium import create_basic_equilibrium
from redox.create_acidic_equilibrium import create_acidic_equilibrium
from chempy import Equilibrium
def test_create_acidic_equilibrium():
    with open('tests/redox_test_data/acidic/forms.txt', 'r') as f:
        oxidants_and_reductors = [line.strip().split('=') for line in list(filter(lambda x: '#' not in x, f.readlines()))]
    with open('tests/redox_test_data/acidic/equilibria.txt', 'r') as f:
        equilibria_lines = list(filter(lambda x: '#' not in x, f.readlines()))
    assert len(equilibria_lines) == len(oxidants_and_reductors)
    length = len(equilibria_lines)
    for i in range(length):
        form1, form2 = oxidants_and_reductors[i]
        created_equilibrium = create_acidic_equilibrium(form1, form2, 1)
        test_equilibrium = Equilibrium.from_string(equilibria_lines[i])
        assert created_equilibrium.reac == dict(test_equilibrium.reac)
        assert created_equilibrium.prod == dict(test_equilibrium.prod)
def test_create_basic_equilibrium():
    with open('tests/redox_test_data/basic/forms.txt', 'r') as f:
        oxidants_and_reductors = [line.strip().split('=') for line in list(filter(lambda x: '#' not in x, f.readlines()))]
    with open('tests/redox_test_data/basic/equilibria.txt', 'r+') as f:
        for _ in oxidants_and_reductors:
            form1, form2 = _
            print(form1, form2)
            equilibrium = create_basic_equilibrium(form1, form2, 1)
            f.write(f.read() + equilibrium.__str__() + '\n')
