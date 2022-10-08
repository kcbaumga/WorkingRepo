#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 23:23:47 2022

@author: kyle
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model

oecd_bill=pd.read_csv("~/.pragai6/.pragai6/lib/data/oecd_bli_2015.csv", thousands=',')
gdp_per_capita=pd.read_csv("~/.pragai6/.pragai6/lib/data/gdp_per_capita.csv", thousands=',', delimiter='\t',
                           encoding='latin1', na_values="n/a")
def prepare_country_stats(oecd_bli, gdp_per_capita):
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"]=="TOT"]
    oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    gdp_per_capita.set_index("Country", inplace=True)
    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita,
                                  left_index=True, right_index=True)
    full_country_stats.sort_values(by="GDP per capita", inplace=True)
    remove_indices = [0, 1, 6, 8, 33, 34, 35]
    keep_indices = list(set(range(36)) - set(remove_indices))
    return full_country_stats[["GDP per capita", 'Life satisfaction']].iloc[keep_indices]
country_stats=prepare_country_stats(oecd_bill, gdp_per_capita)

x=np.c_[country_stats["GDP Per Capita"]]
y=np.c_[country_stats["Life Satisfaction"]]

country_stats.plot(kind='scatter', x="GDP Per Capita", y="Life Satisfaction")
plt.show()

model=sklearn.linear_model.LinearRegression()

model.fit(x,y)

X_new=[[22587]]
print(model.predict(X_new))