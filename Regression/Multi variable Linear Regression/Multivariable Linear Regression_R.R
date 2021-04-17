# Multivariable Linear Regression
dataset = read.csv('50_Startups.csv')


# Encoding Categorical Variable.
dataset$State = factor(dataset$State, levels = c('New York', 'California', 'Florida')
                       labels = c(1,2,3))

# spliting the dataset into train and test
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit , SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split==TRUE)




# Fitting Multiple Linear Regression
regressor=lm(formula = Salary ~.,
             data = training_set)

summary(regressor)

#predicting the test results
y_pred = predict(regressor, newdata = test_set)

#Building the optimal Model using Backward Elimination
regressor=lm(formula = Salary ~R.D.Spend + Administration + Marketing.spend + State,
             data = dataset)
summary(regressor)


regressor=lm(formula = Salary ~R.D.Spend + Administration + Marketing.spend,
             data = dataset)
summary(regressor)


regressor=lm(formula = Salary ~R.D.Spend + Marketing.spend,
             data = dataset)
summary(regressor)

regressor=lm(formula = Salary ~R.D.Spend,
             data = dataset)
summary(regressor)