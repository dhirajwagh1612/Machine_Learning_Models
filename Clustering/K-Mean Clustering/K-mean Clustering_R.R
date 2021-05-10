#Naive Bayes.
setwd('F:/Projects/Machine Learning/ML/Machine_Learning_Models/Clustering/K-Mean Clustering/')



# loading mall dataset.
dataset = read.csv('Mall_Customers.csv')
X = dataset[4:5]


# Using elbow method to find the optimal number of clusters
set.seed(6)
wcss = vector()
for (i in 1:10) sum(kmeans(X,i)$swithinss)
plot(1:10, wcss, type = 'b', main = paste('clusters of clients'), xlab = 'number of clusters', ylab = 'WCSS')

# Applying K means to the mall dataset.
set.seed(29)
kmeans = kmeans(X, 5, iter.max = 300, nstart = 10)



#Visualising data dataset
library(cluster)
clusplot(X,
         kmeans$cluster,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         label = 2,
         plotchar = FALSE,
         span = TRUE,
         main = paste('Clusters of clients'),
         xlab = 'Annual Income',
         ylab = 'Spending')
