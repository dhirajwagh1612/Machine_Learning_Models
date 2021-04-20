# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 12:24:48 2021

@author: Dhiraj Wagh
"""
#Decision Tree regression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values



# fitting decision tree to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X, y)


# predict a new result

y_pred = regressor.predict([[1.5]])



# visualize decision tree regressor model.
X_grid = np.arange(min(X), max(X),0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.xlabel('position')
plt.ylabel('Salary')
plt.title('position vs salary.')
plt.show()