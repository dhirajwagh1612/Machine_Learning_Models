# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 13:19:38 2021

@author: Dhiraj Wagh
"""

# importing packages.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing dataset
dataset = pd.read_csv("Position_Salaries.csv")
X= dataset.iloc[:,1:2].values
y= dataset.iloc[:,2].values     





'''
# spliting dataset
from sklearn.preprocessing import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
'''

# fitting Simple Regression to dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)


# Fitting Polynomial Regression to Dataset



# Visualising the Linear Regression results:
plt.scatter(X, y, color= 'red')
plt.plot(X, lin_reg.predict(X), color='blue')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.title('Level vs salary')
plt.show()

# Visualising the Polynomial Regression Results
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color= 'red')
plt.plot(X, lin_reg_2.predict(X_poly), color='blue')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.title('Level vs salary')
plt.show()


# predicting a new result with linear regression
lin_reg.predict(6.5)


#predecting a new result with polynomial regression
lin_reg_2.predict(poly_reg.fit_transform(6.5))