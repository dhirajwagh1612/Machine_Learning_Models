#Support Vector Regressor.

#reading dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

#fitting Support vector to the dataset.
#install.packages('e1071')
library(e1071)

regressor = svm(formula = salary~.,
                data = dataset,
                type = 'eps-regression')




# predecting a new result.
y_pred = predict(regressor, data.frame(level = 6.5))


# visualise the SVR results.
library(ggplot2)
ggplot()+
  geom_point(aes(x = dataset$Level, y= dataset$Salary), colour = 'red')+
  geom_line(aes(x=dataset$Level, y= predict(regressor, newdata = dataset)), colour = 'blue')+
  ggtitle('truth or bluff(SVR)')+
  xlab('Level')+
  ylab('salary')

