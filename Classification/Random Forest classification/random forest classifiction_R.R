#Random forest classification
setwd('F:/Projects/Machine Learning/ML/Machine_Learning_Models/Classification/Random Forest classification/')



# loading dataset.
dataset = read.csv('Social_Network_Ads.csv')
dataset = dataset[, 3:5]

#Encoding the target variable as factor.
dataset$Purchased = factor(dataset$Purchased, levels = c(0, 1))


#spliting dataset into test and train.
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)


#feature scaling.
training_set[, 2:3] = scale(training_set[, 2:3])
test_set[, 2:3] = scale(test_set[, 2:3])

#fitting random forest classification to the training set
#install.packages('randomForest')
library(randomForest)

classifier = randomForest(x = training_set[-3],
                          y = training_set$Purchased,
                          ntree = 10)


y_pred = predict(classifier, newdata = test_set[-3])


#Making the confusion matrix.
cm = table(test_set[, 3], y_pred)


#visualization of logistic regression.
library(ElemStatLearn)
set = training_set
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('Age', 'EstimatedSalary')
prob_set = predict(classifier, type = 'response', newdata = grid_set)
y_grid = predict(classifier, newdata = grid_set)
plot(set[, -3],
     main = 'random forest classification (Training set)',
     xlab = 'Age', ylab = 'Estimated Salary',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))

# Visualising the Test set results
library(ElemStatLearn)
set = test_set
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('Age', 'EstimatedSalary')
prob_set = predict(classifier, type = 'response', newdata = grid_set)
y_grid = predict(classifier, newdata = grid_set)
plot(set[, -3],
     main = 'random forest classification (Test set)',
     xlab = 'Age', ylab = 'Estimated Salary',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))





plot(classifier)
text(classifier)
