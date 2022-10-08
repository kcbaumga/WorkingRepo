#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 21:45:53 2022

@author: kyle
"""
import numpy as np
a=np.array([1,2,3,4])
a.size
a.dtype

b=np.array([[1,2,3,4], [5,6,7,8]])
b
b.shape

c=np.zeros((3,4), dtype="uint32")
c[0,3]=29
c

d=np.arange(12).reshape(3,4)
d[1]
d[1]=[44,55,66,77]
d

d[:2,:1]

e=np.arange(12)
e[2:1:3]

#e[::2]

f=np.arange(24).reshape(6,2,2)
f[2,:,:]=[[100,100],[100,100]]
f

g=np.random.randint(0,5,(3,4))
g
np.save("random.npy",g)
b=np.load("random.npy")
b
