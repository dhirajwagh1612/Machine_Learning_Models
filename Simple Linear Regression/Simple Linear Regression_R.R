# Simple Linear Regressor
dataset = read.csv('Salary_Data.csv')


library(caTools)
# split dataset into train and test
set.seed(123)
split = sample.split(dataset$YearsExperience, SplitRatio = 1/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == TRUE)

regressor = lm(formula = YearExperience ~.
               data = training_set)

