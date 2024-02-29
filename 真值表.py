# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 08:40:52 2024

@author: student
"""

import itertools

# Define the propositions P and Q
propositions = ['P', 'Q']

# Generate all possible combinations of truth values for P and Q
truth_values = list(itertools.product([True, False], repeat=len(propositions)))

# Define the logical operations
def logical_and(p, q):
    return p and q

def logical_or(p, q):
    return p or q

def logical_implication(p, q):
    return not p or q

def logical_reverse_implication(p, q):
    return p or not q

def logical_equivalence(p, q):
    return p == q

# Print the header of the truth table
print("P\tQ\tP ∧ Q\tP ∨ Q\tP → Q\tP ← Q\tP ↔ Q")

# Iterate through each combination of truth values and print the results
for values in truth_values:
    p, q = values
    print(f"{p}\t{q}\t{logical_and(p, q)}\t{logical_or(p, q)}\t{logical_implication(p, q)}\t{logical_reverse_implication(p, q)}\t{logical_equivalence(p, q)}")