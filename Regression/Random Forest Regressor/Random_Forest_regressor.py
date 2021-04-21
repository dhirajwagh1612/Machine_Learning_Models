# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 11:50:56 2021

@author: Dhiraj Wagh
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Position_Salaries.csv')
X= dataset.iloc[:, 1:2].values
y= dataset.iloc[:, 2].values



# fit the random forest regressor in the dataset.
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(X,y)

#predict the value.
y_pred = regressor.predict([[5.5]])

#visualising data.

X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color = 'red')

plt.title('position vs salary')
plt.xlabel('position level')
plt.ylabel('salary')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.show()