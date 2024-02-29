# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 09:29:08 2024

@author: student
"""

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
x1=(-b+(b**2-4*a*c)**(0.5))/(2*a)
x2=(-b-(b**2-4*a*c)**(0.5))/(2*a)
print("1st root is",x1)
print("2nd root is",x2)
