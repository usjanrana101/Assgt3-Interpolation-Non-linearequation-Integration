#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 00:09:49 2019

@author: jaga
"""

from scipy import integrate
import numpy as np
def f(x):
    return np.exp(x)
print('Integration of exp(x) from 0 to 1 via Romberg Quadrature Method is =:',integrate.romberg(f,0,1))