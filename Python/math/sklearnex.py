#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 22:48:48 2022

@author: kyle
"""
import numpy as np
from sklearn.datasets import load_digits
from sklearn.neural_network import MLPClassifier

d=load_digits()
digits=d["data"]
labels=d["target"]
N=200

idx=np.argsort(np.random.random(len(labels)))
x_test, y_test= digits[idx[:N]], labels[idx[:N]]
x_train, y_train=digits[idx[N:]], labels[idx[N:]]

clf=MLPClassifier(hidden_layer_sizes=(128,))
clf.fit(x_train, y_train)

score=clf.score(x_test, y_test)
pred=clf.predict(x_test)
err=np.where(y_test!=pred)[0]
print("score :", score)
print("Errors:")
print("Actual: ", y_test[err])
print("Predicted: ", pred[err])