#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 00:08:44 2022

@author: kyle
"""
import numpy as np
nb=0
N=10000
for i in range(N):
    s=np.random.randint(0,50,3)
    fail=False
    for t in range(3):
        if (s[t]<4):
            fail=True
    if (not fail):
        nb+=1
print("NO Boston in Fall: = %0.4f" % (nb/N,))