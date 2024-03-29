# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:24:58 2021

@author: Dhiraj Wagh.
"""
# importing libraries.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# importing dataset.
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:,[3,4]].values


# Using the elbow method to find the optimal number of clusters.
from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11), wcss)
plt.title('the elbow method')
plt.xlabel('number of clusters')
plt.ylabel('WCSS')
plt.show()


#Applying k-means to the mall dataset
kmeans = KMeans(n_clusters = 5, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
y_kmeans = kmeans.fit(X)


#visualizing the cluster.
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans== 0,1],s= 100, c='red', label='Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans== 1,1],s= 100, c='blue', label='Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans== 2,1],s= 100, c='green', label='Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans== 3,1],s= 100, c='cyan', label='Cluster 4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans== 4,1],s= 100, c='magenta', label='Cluster 5')

plt.scatter(kmeans.cluster_centers__[:, 0], kmeans.cluster_centers__[:,1], s= 300, c='yellow', label='centroid')
plt.title('clusters of clients')
plt.xlabel('Annual Income(k$')
plt.ylabel('Spending Score (1-100')
plt.legend()
plt.show()