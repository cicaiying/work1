# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 09:21:03 2024

@author: student
"""

row = "{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}"
print(row.format("P", "Q", "P ∧ Q", "P ∨ Q", "P → Q", "P ← Q", "P ↔ Q"))
print(row.format("F", "F", "F", "F", "T", "T", "T"))
print(row.format("F", "T", "F", "T", "T", "F", "F"))
print(row.format("T", "F", "F", "T", "F", "T", "F"))
print(row.format("T", "T", "T", "T", "T", "T", "T"))