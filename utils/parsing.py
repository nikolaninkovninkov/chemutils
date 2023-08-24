from pyparsing import (Suppress, Word, nums, alphas, Regex, Forward, Group, 
                        Optional, OneOrMore, ParseResults)
from collections import defaultdict
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from general_chemistry.periodic_data import get_atomic_number
def _get_charge(compound: str):
    plus_count = compound.count('+')
    minus_count = compound.count('-')
    if plus_count + minus_count == 0:
        return 0
    if plus_count + minus_count > 1:
        raise ValueError("More than one plus or minus")
    charge_symbol = plus_count*'+' + minus_count*'-'
    charge_sign = plus_count - minus_count
    charge_number_as_str = compound.split(charge_symbol)[1]
    if charge_number_as_str == '':
        return charge_sign
    if not charge_number_as_str.isdigit():
        raise ValueError("Plus or minus must not be followed by anything other than digits")
    charge_number = int(charge_number_as_str)
    return charge_number * charge_sign
def formula_to_atomic_composition(compound: str):
    """
    BNF for simple chemical formula (no nesting)

        integer :: '0'..'9'+
        element :: 'A'..'Z' 'a'..'z'*
        term :: element [integer]
        formula :: term+


    BNF for nested chemical formula

        integer :: '0'..'9'+
        element :: 'A'..'Z' 'a'..'z'*
        term :: (element | '(' formula ')') [integer]
        formula :: term+

    """
    #Preprocessing
    compound = compound.replace('[', '(').replace(']', ')')
    #Electrons
    if compound == 'e-':
        return {'charge': -1}
    LPAR,RPAR = map(Suppress,"()")
    integer = Word(nums)

    # add parse action to convert integers to ints, to support doing addition 
    # and multiplication at parse time
    integer.setParseAction(lambda t:int(t[0]))

    element = Word(alphas.upper(), alphas.lower())
    # or if you want to be more specific, use this Regex
    # element = Regex(r"A[cglmrstu]|B[aehikr]?|C[adeflmorsu]?|D[bsy]|E[rsu]|F[emr]?|"
    #                 "G[ade]|H[efgos]?|I[nr]?|Kr?|L[airu]|M[dgnot]|N[abdeiop]?|"
    #                 "Os?|P[abdmortu]?|R[abefghnu]|S[bcegimnr]?|T[abcehilm]|"
    #                 "Uu[bhopqst]|U|V|W|Xe|Yb?|Z[nr]")

    # forward declare 'formula' so it can be used in definition of 'term'
    formula = Forward()

    term = Group((element | Group(LPAR + formula + RPAR)("subgroup")) + 
                    Optional(integer, default=1)("mult"))

    # define contents of a formula as one or more terms
    formula << OneOrMore(term)


    # add parse actions for parse-time processing

    # parse action to multiply out subgroups
    def multiplyContents(tokens):
        t = tokens[0]
        # if these tokens contain a subgroup, then use multiplier to
        # extend counts of all elements in the subgroup
        if t.subgroup:
            mult = t.mult
            for term in t.subgroup:
                term[1] *= mult
            return t.subgroup
    term.setParseAction(multiplyContents)

    # add parse action to sum up multiple references to the same element
    def sumByElement(tokens):
        elementsList = [t[0] for t in tokens]

        # construct set to see if there are duplicates
        duplicates = len(elementsList) > len(set(elementsList))

        # if there are duplicate element names, sum up by element and
        # return a new nested ParseResults
        if duplicates:
            ctr = defaultdict(int)
            for t in tokens:
                ctr[t[0]] += t[1]
            return ParseResults([ParseResults([k,v]) for k,v in ctr.items()])
    formula.setParseAction(sumByElement)
    results = dict(formula.parseString(compound).asList())
    return {**results, 'charge' : _get_charge(compound)}
def formula_to_composition(compound: str):
    atomic_composition = formula_to_atomic_composition(compound)
    composition = {}
    for k, v in atomic_composition.items():
        if k == 'charge':
            if v != 0:
                composition[0] = v
            continue
        composition[get_atomic_number(k)] = v
    return composition
