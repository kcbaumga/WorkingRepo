#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 22:14:36 2022

@author: kyle
"""
import numpy as np
import scipy
from scipy.stats import ttest_ind
a=np.random.normal(0,1,1000)
b=np.random.normal(0,0.5,1000)
c=np.random.normal(0.1,1,1000)
ttest_ind(a,b)
ttest_ind(a,c)

import matplotlib.pylab as plt

x=np.random.random(100)
x
#plt.plot(x)
#plt.show()


from mpl_toolkits.mplot3d import Axes3D
u=np.random.random(20)
y=np.random.random(20)
z=np.random.random(20)
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.scatter(u,y,z)
plt.show()

