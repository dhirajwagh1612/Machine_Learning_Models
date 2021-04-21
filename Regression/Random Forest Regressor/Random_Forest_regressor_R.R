#random forest regressor.


dataset = read.csv('Salary_Position.csv')
datset[2:3]

#fitting the random forest model.

library(randomForest)
set.seed(1234)

# create regreesor here.
#install.packages('randomForest')

regressor = randomForest(x = dataset[1], 
                         y = dataset$Salary,
                         ntrees = 10)
# prediction
y_pred = predict(regressor, data.frame(Level = 6.5))





# data visualize for random forest.
library(ggplot2)
X_grid = seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot()+
  geom_point(aes(x = dataset$Level, y=dataset$Salary), 
             color = 'red')+
  geom_point(aes(x = X_grid, y=predict(regressor, newdata = data.frame(Level = 6.5)))
             color = 'blue')+
  ggtitle('Level vs Salary("Random Forest")')+
  xlab('Level')+
  ylab('salary')