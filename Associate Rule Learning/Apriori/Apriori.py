# -*- coding: utf-8 -*-
"""
Created on Sun May 16 12:44:10 2021

@author: Dhiraj Wagh
"""

# Apriori Algorithms
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Importing the dataset
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header=None)
transactions = []
for i in range (0,7501):
    transactions.append([str(dataset.values[i, j]) for j in range(0,20)])
    
#training Apriori on the dataset.
from apyori import apriori
rules = apriori(transactions, min_support = 0.00279962, min_confidance = 0.2, min_lift = 3, min_length = 2)


# Visualizing the results.
results = list(rules)
    

