dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]


library('caTools')

# fitting linear regression to dataset.
lin_reg = lm(formula = Salary ~.,
             data = dataset)

summary(lin_reg)
# fitting polynomial regressor
dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4
dataset$Level5 = dataset$Level^5
poly_reg = lm(formula = Salary ~.,
              data=dataset)

Summary(poly_reg)


#visualising the linear Regression Result
library(ggplot2)
ggplot() +
  geom_point(aes(x= dataset$Level, y=dataset$Salary),
             colour = 'red')+
  geom_line(aes(x= dataset$Level, y= predict(lin_reg, newdata = dataset)),
            colour = 'blue')+
ggtitle('Truth or Bluff')+
xlab('Level')+
ylab('salary')

# visualising the polynomial regression.
library(ggplot2)
ggplot() +
  geom_point(aes(x= dataset$Level, y=dataset$Salary),
             colour = 'red')+
  geom_line(aes(x= dataset$Level, y= predict(poly_reg, newdata = dataset)),
            colour = 'blue')+
ggtitle('Truth or Bluff')+
xlab('Level')+
ylab('salary') 

#predicting a new result with Linear Regression.

y_pred = predict(lin_reg, data.frame(Level = 6.5))

#predicting a new result with Polynomial Regression.
y_pred = predict(poly_reg, data.frame(Level = 6.5,
                                      Level = 6.5^2,
                                      Level = 6.5^3,
                                      Level = 6.5^4))