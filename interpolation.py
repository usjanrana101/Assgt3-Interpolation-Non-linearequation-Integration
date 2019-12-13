#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 17:32:54 2019

@author: jagannath rana
"""

from matplotlib import pyplot as plt
import numpy as np
import scipy.interpolate as si
x=[0,1,2,3,4,5]      # Given Data 
y=[1.0,2.0,1.0,0.5,4.0,8.0]
spl_lin= si.InterpolatedUnivariateSpline(x,y,k=1)
spl_quad= si.InterpolatedUnivariateSpline(x,y,k=2)    # this InterpolatedUnivariateSpline()  returns the spline-interpolated function
spl_cubic= si.InterpolatedUnivariateSpline(x,y,k=3)
lag=si.lagrange(x,y)
xnew=np.arange(0,5,.001)
plt.scatter(x,y,label='Data')
plt.plot(xnew,spl_lin(xnew),xnew,spl_quad(xnew),xnew,spl_cubic(xnew),xnew,lag(xnew),'--')
plt.legend(['lin_spline','quad_spline','cubic_spline','lagrange'],loc='best')
plt.title('Spline and Lagrange Interpolated Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
