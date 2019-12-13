#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 20:10:36 2019

@author: jaga
"""

from scipy import optimize
from numpy import sin,cos,exp
def f(x):
    return sin(cos(exp(x)))

def devf(x):  # derivative of the given function
    return -cos(cos(exp(x)))*sin(exp(x))*exp(x)
root1=optimize.newton(f,-1.0,devf)
print ('When initial guess is x=-1 using newton_raphson , root is',root1) 
print('value of f(',root1,') is =:',f(root1)) # checking whether root is correct or not
root2=optimize.newton(f,-0.1,devf)
print ('When initial guess is x=-0.1 using newton_raphson, root is',root2)
print('value of f(',root2,') is =:',f(root2))