#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 23:25:52 2022

@author: kyle
"""
import numpy as np
match=0
for i in range(100000):
    a=np.random.randint(0,364)
    b=np.random.randint(0,364)
    if (a==b):
        match+=1
print("Probability of a match = %.6f" % (match/100000,))