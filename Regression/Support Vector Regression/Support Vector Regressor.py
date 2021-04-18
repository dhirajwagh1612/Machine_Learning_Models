# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 12:55:19 2021

@author: Dhiraj Wagh
"""

# Support Vector Regressor.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('Position_Salaries.csv')


X = dataset.iloc[:, 1:2].values
y=dataset.iloc[:, 2].values



#feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)


# fitting model in SVM
from sklearn.svm import SVR
regressor = SVR(kernel='rbf')
regressor.fit(X,y)



#predicting new result.
y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array([[6.5]]))))



#visualization SVR result
plt.scatter(X,y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('salary vs position')
plt.xlabel('position')
plt.ylabel('salary')


