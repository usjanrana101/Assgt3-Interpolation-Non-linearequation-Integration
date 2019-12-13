#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 00:02:30 2019

@author:ritambasu61
"""

from scipy import integrate
import numpy as np
def g(z):
    return np.exp(z)
x=np.arange(0,1,.001)
y=g(x)
print('Integration of exp(x) from 0 to 1 (by simpson-1/3) =:',integrate.simps(y,x))