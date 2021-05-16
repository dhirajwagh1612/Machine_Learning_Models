# -*- coding: utf-8 -*-
"""
Created on Sun May 16 13:33:21 2021

@author: Dhiraj Wagh
"""

#Importing the Libraries.
import numpy as np
import pandas as pd
import matplotlib.pylab as plt

dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# IMPLEMENTING THE ALGORITHM RANDEM SELECTION
import random
N= 10000
d= 10
ads_selected = []
total_reward = 0
for n in range(0,N):
    ad = random.randrange(d)
    ads_selected.append(ad)
    reward = dataset.values[n, ad]
    total_reward = total_reward + reward
    
    
    
#Visualizing the results - Histogram
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()
