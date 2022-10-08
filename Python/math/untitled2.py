#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 00:11:08 2022

@author: kyle
"""
import pandas as pd
nba_housing=pd.read_csv("~/.pragai6/.pragai6/lib/data/nba_2017_att_val_elo_housing.csv")
nba_housing.columns
#num_df=nba_housing.loc[:,\
#                       ["TOTAL_ATTENDANCE_MILLIONS", "ELO", "VALUE_MILLIONS", "MEDIAN_HOME_PRICE_COUNTY_MILLONS"]]
num_df = nba_housing.loc[:,["TOTAL_ATTENDANCE_MILLIONS","ELO",  "VALUE_MILLIONS", "MEDIAN_HOME_PRICE_COUNTY_MILLONS"]]
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
print(scaler.fit(num_df))
print(scaler.transform(num_df))
MinMaxScaler(copy=True, feature_range=(0,1))
from sklearn.cluster import KMeans
k_means = KMeans(n_clusters=3)
kmeans = k_means.fit(scaler.transform(num_df))
nba_housing['cluster'] = kmeans.labels_
nba_housing.head()
nba_housing.to_csv("~/.pragai6/.pragai6/lib/data/nba_2017_write.csv")