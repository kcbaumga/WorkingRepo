#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 22:15:35 2022

@author: kyle
"""

import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
color = sns.color_palette()
#%matplotlib inline


nba_br = pd.read_csv("~/.pragai6/.pragai6/lib/data/nba_2017_br.csv")
nba_atten=pd.read_csv("~/.pragai6/.pragai6/lib/data/nba_2017_attendance.csv")
nba_endor=pd.read_csv("~/.pragai6/.pragai6/lib/data/nba_2017_endorsements.csv")
nba_valu=pd.read_csv("~/.pragai6/.pragai6/lib/data/nba_2017_team_valuations.csv")
nba_salary=pd.read_csv("~/.pragai6/.pragai6/lib/data/nba_2017_salary.csv")
nba_pie=pd.read_csv("~/.pragai6/.pragai6/lib/data/nba_2017_pie.csv")
nba_plus=pd.read_csv("~/.pragai6/.pragai6/lib/data/nba_2017_real_plus_minus.csv")
nba_elo=pd.read_csv("~/.pragai6/.pragai6/lib/data/nba_2017_elo.csv")

attendance_valuation_df=\
    nba_atten.merge(nba_valu, how="inner", on="TEAM")
    
attendance_valuation_df.head()

from IPython.core.display import display, HTML
#display(HTML("<style>.\
#            container{width:100% !important; }</style>"));\
#sns.pairplot(attendance_valuation_df, hue="TEAM")
corr=attendance_valuation_df.corr()
#sns.heatmap(corr, xticklabels=corr.columns.values, \ 
#            yticklabels=corr.columns.values)
#valuations=attendance_valuation_df.\
#   pivot("TEAM", "TOTAL_MILLIONS", "VALUE_MILLIONS")
#plt.subplots(figsize=(20,15))
#ax=plt.axes()
#ax.set_title("NBA Team Average Attendance vs\
#             Valuation in Millions: 2016-2017 Season")
#sns.heatmap(valuations, linewidth=1, annot=True, fmt='g')
#import statsmodels as smf
results=smf.ols('VALUE_MILLIONS ~TOTAL_MILLIONS', data=attendance_valuation_df).fit()
#print(results.summary())


#sns.residplot(y="VALUE_MILLIONS", x="TOTAL_MILLIONS",\
#              data=attendance_valuation_df)
attendance_valuation_predictions_df = attendance_valuation_df.copy()
attendance_valuation_predictions_df["predicted"] = results.predict()
import statsmodels
rmse=statsmodels.tools.eval_measures.rmse(attendance_valuation_predictions_df["predicted"],attendance_valuation_predictions_df["VALUE_MILLIONS"])
#rmse

#sns.lmplot(x="predicted", y="VALUE_MILLIONS", data=attendance_valuation_predictions_df)
nba_housing=pd.read_csv("~/.pragai6/.pragai6/lib/data/nba_2017_att_val_elo_housing.csv"); nba_housing.head()
nba_housing.columns
num_df=nba_housing.loc[:,\
                       ["TOTAL_ATTENDANCE_MILLIONS", "ELO", "VALUE_MILLIONS", "MEDIAN_HOME_PRICE_COUNTY_MILLONS"]]
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
scaler.fit(num_df)
#print(scaler.fit(num_df))
#print(scaler.transform(num_df))

from sklearn.cluster import KMeans
k_means=KMeans(n_clusters=3)
kmeans=k_means.fit(scaler.transform(num_df))
nba_housing['cluster']=kmeans.labels_
nba_housing.head()

