# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 17:42:53 2021

@author: Dhiraj Wagh
"""
# importing packages.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# importing dataset
dataset = pd.read_csv('50_Startups.csv')
X=dataset.iloc[:, :-1].values
y=dataset.iloc[:, 4].values

#Encoding categorical Data.
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] =   labelencoder_X.fit_transform(X[:, 3])
oneHotEncoder = OneHotEncoder(categorical_features=[3])
X=oneHotEncoder.fit_transform(X).toarray()

#Avoiding the dummy variable trap
X=X[:, 1:]

#Spliting the dataset into the training set  and test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X,y ,test_size = 0.2, random_state = 0)

#fitting multiple linear regression to training set
from sklearn.preprocessing import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#predecting the test set result
y_pred = regressor.predict(y_test)


# Building the optimal model using Backward Elimination
import statsmodels.formula.api as sm
X=np.append(arr=np.ones((50,1)).astype(int), values=X, axis = 1)
X_opt = X[:, [0,1,2,3,4,5]]
regression_OLS = sm.OLS(Endog = y, exog = X_opt).fit()
regression_OLS.summary()
X_opt = X[:, [0,1,3,4,5]]
regression_OLS = sm.OLS(endod = y, exog = X_opt).fit()
regression_OLS.summary()
X_opt = X[:, [0,3,4,5]]
regression_OLS = sm.OLS(endod = y, exog = X_opt).fit()
regression_OLS.summary()
X_opt = X[:, [0,3,5]]
regression_OLS = sm.OLS(endod = y, exog = X_opt).fit()
regression_OLS.summary()
X_opt = X[:, [0,3]]
regression_OLS = sm.OLS(endod = y, exog = X_opt).fit()
regression_OLS.summary()