#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 00:14:59 2019

@author: jaga
"""

import numpy as np
def f(x):
    return np.exp(x)
x=np.arange(0,1,.01)
y=f(x)
print('Integration of exp(x) from 0 to 1 via Trapezoidal Method is =:',np.trapz(y,x))