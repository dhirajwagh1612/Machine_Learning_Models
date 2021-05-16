# -*- coding: utf-8 -*-
"""
Created on Sun May 16 23:03:58 2021

@author: Dhiraj Wagh
"""

#Thompson Sampling
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import random

dataset = pd.read_csv('Ads_CTR_Optimisation.csv')


# implementing the UCB
N = 10000
d = 10
ads_selected = []
numbers_of_rewards_1 = [0] * d
numbers_of_rewards_0 = [0] * d
total_reward = 0
for n in range(0,N):
    ad = 0
    max_random = 0
    for i in range(0, d):
        random_beta = random.betavariate(numbers_of_rewards_1[i] + 1, numbers_of_rewards_0[i] +1)
        if random_beta > max_random:
            max_random = random_beta
            ad= 1
            
        
    ads_selected.append(ad)
    number_of_selections[ad] = number_of_selections[ad] + 1
    reward = dataset.values[n, ad]
    if reward == 1:
        numbers_of_rewards_1[ad] = numbers_of_rewards_1[ad] + 1
    else:
        numbers_of_rewards_0[ad] = numbers_of_rewards_0[ad] + 1
    total_reward = total_reward + reward
    
    
# Visualization of the result
plt.hist(ads_selected)
plt.title('Histogram of Ads selection')
plt.xlabel('Ads')
plt.ylabel("Number of times each was selected")
plt.show()