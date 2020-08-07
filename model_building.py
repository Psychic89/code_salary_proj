#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 14:22:19 2020

@author: Robert
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('eda_data.csv')

# Choose relevant columns
df.columns

df_model = df[['Bewertung','Firmengröße', 'Rechtsform', 'Industriezweig', 'Branche', 'Umsatz', 'num_konkurrenten', 'job_city', 'job_country', 'job_at_hq', 'company_age', 'python_yn', 'R_yn', 'spark', 'aws', 'excel', 'job_simp', 'desc_len']]

# get dummy data
df_dum = pd.get_dummies(df_model)

# train test split
# train test split 
from sklearn.model_selection import train_test_split

X = df_dum.drop('Bewer', axis =1)
y = df_dum.Bewertung.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# multiple linear regression 
import statsmodels.api as sm

X_sm = X = sm.add_constant(X)
model = sm.OLS(y,X_sm)
model.fit().summary()

from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score

lm = LinearRegression()
lm.fit(X_train, y_train)

np.mean(cross_val_score(lm,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3))

# lasso regression
lm_l = Lasso()
np.mean(cross_val_score(lm_l,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3))

alpha = []
error = []

for i in range(1, 100):
    alpha.append(i/100)
    lml = Lasso(alpha=(i/100))
    error.append(np.mean(cross_val_score(lm_l,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3)))
    
plt.plot(alpha,error)

err = tuple(zip(alpha,error))
df_err = pd.DataFrame(err, columns = ['alpha','error'])
df_err[df_err.error == max(df_err.error)]

# random forest
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()

np.mean(cross_val_score(rf, X_train, y_train, scoring = 'neg_mean_absolute_error', cv = 3))
