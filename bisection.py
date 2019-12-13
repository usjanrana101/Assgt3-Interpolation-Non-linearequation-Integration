#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 19:59:38 2019

@author: jaga
"""
from scipy import optimize
from numpy import sin,cos,exp
def f(x):
    return sin(cos(exp(x)))
root=optimize.bisect(f,-1,1)
print ('Using bisection method root is =:',root)
print ('value of f(x) at the root is',f(root))