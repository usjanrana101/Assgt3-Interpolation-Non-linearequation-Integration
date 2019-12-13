#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 00:00:20 2019

@author:ritambasu61
"""
from scipy import optimize
from numpy import sin,cos,exp
def f(x):
    return sin(cos(exp(x)))
r=optimize.newton(f,-0.1)
print ('For initial guess is x=-0.1 , root is',r)
print ('value of f(x) at',r,'is:',f(r))
