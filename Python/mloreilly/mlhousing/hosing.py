#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 15:21:21 2022

@author: kyle
"""

import os
import tarfile
import urllib.request


#DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/kcbaumga/WorkingRepo/main/Python/mloreilly/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"
#Download url onto path
def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    os.makedirs(housing_path, exist_ok=True)
    tgz_path=os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz=tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()
fetch_housing_data()
import pandas as pd

#Grab housing csv
def load_housing_data(housing_path=HOUSING_PATH):
    csv_path=os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)
housing=load_housing_data()
#housing.head()
#housing.info()

#housing["ocean_proximity"].value_counts()

#housing.describe()

#Histograms
#import matplotlib.pyplot as plt
#housing.hist(bins=50, figsize=(20,15))
#plt.show()

import numpy as np


#Test Set Random

def split_train_test(data, test_ratio):
    shuffled_indices=np.random.permutation(len(data))
    test_set_size=int(len(data)*test_ratio)
    test_indices=shuffled_indices[:test_set_size]
    train_indices=shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]
train_set, test_set=split_train_test(housing, .2)
len(train_set), len(test_set)

from zlib import crc32
#Maintain dataset
def test_set_check(identifier, test_ratio):
    return crc32(np.int64(identifier)) & 0xffffffff <test_ratio*2**32

def split_train_test_by_id(data, test_ratio, id_column):
    ids=data[id_column]
    in_test_set=ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]

housing_with_id=housing.reset_index()
housing_with_id["id"]=housing["longitude"]*1000+housing["latitude"]
train_set, test_set= split_train_test_by_id(housing_with_id, .2, "id")


#Other method for above
#from sklearn.model_selection import train_test_split

#train_set, test_set=train_test_split(housing, test_size=.2, random_state=42)

#ensure representative of dataset
housing["income_cat"]=pd.cut(housing["median_income"],
                             bins=[0.,1.5,3.0,4.5,6., np.inf],
                             labels=[1,2,3,4,5])

#housing["income_cat"].hist()

from sklearn.model_selection import StratifiedShuffleSplit
split=StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set=housing.loc[train_index]
    strat_test_set=housing.loc[test_index]

strat_test_set["income_cat"].value_counts() / len(strat_test_set)

for set_ in (strat_train_set, strat_test_set):
    set_.drop("income_cat", axis=1, inplace=True)

housing=strat_train_set.copy()
#housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4, s=housing["population"]/100,
 #            label="population", figsize=(10,7), c="median_house_value", cmap=plt.get_cmap("jet"),
 #            colorbar=True,
 #            )
#plt.legend()

#standard correlation coefficient
corr_matrix=housing.corr()
corr_matrix["median_house_value"].sort_values(ascending=False)


#will compare 11 col x 11 col by default
#from pandas.plotting import scatter_matrix
attributes=["median_house_value", "median_income", "total_rooms", "housing_median_age"]
#scatter_matrix(housing[attributes], figsize=(12,8))

housing["rooms_per_household"]=housing["total_rooms"]/housing["households"]
housing["bedrooms_per_room"]=housing["total_bedrooms"]/housing["total_rooms"]
housing["population_per_household"]=housing["population"]/housing["households"]
corr_matrix=housing.corr()
corr_matrix["median_house_value"].sort_values(ascending=False)

#clean training set
housing=strat_train_set.drop("median_house_value", axis=1)
housing_labels=strat_train_set["median_house_value"].copy()

#Cleaning Data
housing.dropna(subset=["total_bedrooms"])
housing.drop("total_bedrooms", axis=1)
median=housing["total_bedrooms"].median()
housing["total_bedrooms"].fillna(median, inplace=True)

#Replace missing values
from sklearn.impute import SimpleImputer
imputer=SimpleImputer(strategy="median")
housing_num=housing.drop("ocean_proximity", axis=1)
imputer.fit(housing_num)

#same result w/ these 2
imputer.statistics_
housing_num.median().values

x=imputer.transform(housing_num)
housing_tr=pd.DataFrame(x, columns=housing_num.columns,
                        index=housing_num.index)

housing_cat=housing[["ocean_proximity"]]
housing_cat.head(10)

#text to num
from sklearn.preprocessing import OrdinalEncoder
ordinal_encoder=OrdinalEncoder()
housing_cat_encoded=ordinal_encoder.fit_transform(housing_cat)
housing_cat_encoded[:10]

ordinal_encoder.categories_

#Need to create multi binary columns dummy attributes. From scikit

from sklearn.preprocessing import OneHotEncoder
cat_encoder=OneHotEncoder()
housing_cat_1hot=cat_encoder.fit_transform(housing_cat)
housing_cat_1hot
#encoded binary of each value in list
housing_cat_1hot.toarray()

#Transformer Class add combined attributes
from sklearn.base import BaseEstimator, TransformerMixin

#rooms_ix, bedrooms_ix, population_ix, households_ix=3,4,5,6
#Dynamic method for indexes
col_names = "total_rooms", "total_bedrooms", "population", "households"
rooms_ix, bedrooms_ix, population_ix, households_ix = [
    housing.columns.get_loc(c) for c in col_names]
class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True): # no *args or **kargs
        self.add_bedrooms_per_room = add_bedrooms_per_room
    def fit(self, X, y=None):
        return self  # nothing else to do
    def transform(self, X):
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:, households_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household,
                         bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]
attr_adder=CombinedAttributesAdder(add_bedrooms_per_room=False)
housing_extra_attribs=attr_adder.transform(housing.values)

#Sklearn Transformation Pipeline
#Fit scalers to training data only

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

num_pipeline=Pipeline([
    ('imputer', SimpleImputer(strategy="median")),
    ('attribs_adder', CombinedAttributesAdder()),
    ('std_scaler', StandardScaler()),
    ])

housing_num_tr=num_pipeline.fit_transform(housing_num)


#Column transformer handles all columns not handling differently
from sklearn.compose import ColumnTransformer

num_attribs=list(housing_num)
cat_attribs=["ocean_proximity"]
#requires tuple, transformer, columns it will targer
full_pipeline=ColumnTransformer([
    ("num", num_pipeline, num_attribs),
    ("cat", OneHotEncoder(), cat_attribs),
    ])
housing_prepared=full_pipeline.fit_transform(housing)


#Selecting and training model
#First training a linear regressor
from sklearn.linear_model import LinearRegression

lin_reg=LinearRegression()
lin_reg.fit(housing_prepared, housing_labels)
#Trying data now
some_data=housing.iloc[:5]
some_labels=housing_labels[:5]
some_data_prepared=full_pipeline.transform(some_data)

#Comparson of two of these
#print("Predictions", lin_reg.predict(some_data_prepared))
#print("Labels:", list(some_labels))

#Checks prediction over known labels
divisionoftwo=lin_reg.predict(some_data_prepared)/list(some_labels)
#print(divisionoftwo)

#mean squared error
#Grabbing typical error from RMSE
from sklearn.metrics import mean_squared_error
housing_predictions=lin_reg.predict(housing_prepared)
lin_mse=mean_squared_error(housing_labels, housing_predictions)
lin_rmse=np.sqrt(lin_mse)
lin_rmse
#68000 average error... not the best 
#underfit on training data

#Try a DescisionTreeRegressor
from sklearn.tree import DecisionTreeRegressor
tree_reg=DecisionTreeRegressor()
tree_reg.fit(housing_prepared, housing_labels)
#print("Prediction", tree_reg.predict(some_data_prepared))
#print("Labels", list(some_labels))
housing_predictions=tree_reg.predict(housing_prepared)
tree_mse=mean_squared_error(housing_labels, housing_predictions)
tree_rmse=np.sqrt(tree_mse)
tree_rmse
#0 error, probably overfit

#cross validation evaluation
from sklearn.model_selection import cross_val_score
scores=cross_val_score(tree_reg, housing_prepared, housing_labels,
                       scoring="neg_mean_squared_error", cv=10)
tree_rmse_scores=np.sqrt(-scores)
#utility function, scoring opposite of MSE, why it is -scores
def display_scores(scores):
    print("Scores:", scores)
    print("Mean:", scores.mean())
    print("Standard Deviation:", scores.std())
#display_scores(tree_rmse_scores)

#Estimates performance of model
#Now compute same score of Linear Regression model prior

lin_scores=cross_val_score(lin_reg, housing_prepared, housing_labels,
                           scoring="neg_mean_squared_error", cv=10)
lin_rmse_scores=np.sqrt(-lin_scores)
#display_scores(lin_rmse_scores)

#Trying Random Forest Model now
print("MADE IT HERE")
from sklearn.ensemble import RandomForestRegressor
forest_reg = RandomForestRegressor(n_estimators=100, random_state=42)
forest_reg.fit(housing_prepared, housing_labels)


housing_predictions = forest_reg.predict(housing_prepared)
forest_mse = mean_squared_error(housing_labels, housing_predictions)
forest_rmse = np.sqrt(forest_mse)
forest_rmse



forest_scores = cross_val_score(forest_reg, housing_prepared, housing_labels,
                                scoring="neg_mean_squared_error", cv=10)
forest_rmse_scores = np.sqrt(-forest_scores)
#display_scores(forest_rmse_scores)
#promising, score on trainstill might be over fitting
#import joblib
#joblib.dump(my_model, "my_model.pkl")
#my_model_loaded=joblib.load("my_moel.pkl")

#Fine Tuning
#Grid Search to mess with hyper parameters for fine tuning
from sklearn.model_selection import GridSearchCV
param_grid=[
    {'n_estimators': [3,10,30],
     'max_features':[2,4,6,8]},
    {'bootstrap':[False], 'n_estimators':[3,10], 'max_features':[2,3,4]},
    ]
forest_reg = RandomForestRegressor(random_state=42)
grid_search=GridSearchCV(forest_reg, param_grid, cv=5,
                         scoring='neg_mean_squared_error',
                         return_train_score=True)
grid_search.fit(housing_prepared, housing_labels)

#Finds best parameters
#grid_search.best_params_
#direct method for best estimator
grid_search.best_estimator_
cvres=grid_search.cv_results_
#for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
#    print(np.sqrt(-mean_score), params)
#Improved score
#pd.DataFrame(grid_search.cv_results_)


#Possible Randomized Search Approach
#from sklearn.model_selection import RandomizedSearchCV
#from scipy.stats import randint

#param_distribs = {
#        'n_estimators': randint(low=1, high=200),
#        'max_features': randint(low=1, high=8),
#    }

#forest_reg = RandomForestRegressor(random_state=42)
#rnd_search = RandomizedSearchCV(forest_reg, param_distributions=param_distribs,
#                                n_iter=10, cv=5, scoring='neg_mean_squared_error', random_state=42)
#rnd_search.fit(housing_prepared, housing_labels)
#cvres = rnd_search.cv_results_
#for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
#    print(np.sqrt(-mean_score), params)

feature_importances=grid_search.best_estimator_.feature_importances_
#print(feature_importances)


#Importance scores with attributes. Consider dropping location values besides Inland
extra_attribs=["rooms_per_hhold", "pop_per_hhold", "bedrooms_per_room"]
cat_encoder=full_pipeline.named_transformers_["cat"]
cat_one_hot_attribs=list(cat_encoder.categories_[0])
attributes=num_attribs+extra_attribs+cat_one_hot_attribs
print(sorted(zip(feature_importances, attributes), reverse=True))

#Evaluate on Test Set
final_model=grid_search.best_estimator_

x_test=strat_test_set.drop("median_house_value", axis=1)
y_test=strat_test_set["median_house_value"].copy()

x_test_prepared=full_pipeline.transform(x_test)
final_predictions=final_model.predict(x_test_prepared)

my_model=final_predictions
import joblib
joblib.dump(my_model, "Python/mloreilly/mlhousing/my_model.pkl")
my_model_loaded = joblib.load("Python/mloreilly/mlhousing/my_model.pkl")