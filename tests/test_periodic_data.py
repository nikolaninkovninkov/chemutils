import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from periodic_data import get_atomic_number, get_relative_molecular_mass
from utils.diff import diff
def test_get_atomic_number():
    # Test valid element name in different capitalizations
    assert get_atomic_number("Hydrogen") == 1
    assert get_atomic_number("hYdrOgen") == 1
    assert get_atomic_number("HYDROGEN") == 1

    # Test valid element symbol in different capitalizations
    assert get_atomic_number("He") == 2
    assert get_atomic_number("hE") == 2
    assert get_atomic_number("HE") == 2

    # Test invalid element name
    ERR_MESSAGE = "Element not found in the periodic table"
    try:
        get_atomic_number("NonexistentElement")
    except ValueError as e:
        assert str(e) == ERR_MESSAGE

    # Test invalid element symbol
    try:
        get_atomic_number("Xz")
    except ValueError as e:
        assert str(e) == ERR_MESSAGE

    # Test case-insensitive invalid element name
    try:
        get_atomic_number("NonExistent")
    except ValueError as e:
        assert str(e) == ERR_MESSAGE

    # Test case-insensitive invalid element symbol
    try:
        get_atomic_number("XX")
    except ValueError as e:
        assert str(e) == ERR_MESSAGE
def test_get_relative_molecular_mass():
    EPSILON = 1e-10
    assert diff(get_relative_molecular_mass({1: 2, 8: 1}), 18.015) < EPSILON
    assert diff(get_relative_molecular_mass({6: 1, 8:2}), 44.009) < EPSILON
    assert diff(get_relative_molecular_mass({17: 1}), 35.453) < EPSILON