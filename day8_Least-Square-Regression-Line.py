# Linear Regression
# Reference: https://en.wikipedia.org/wiki/Linear_regression
# Task: Find y=f(x)=f(80)

import statistics as st

X=[95,85,80,70,60]
Y=[85,95,70,65,70]
n=len(X)

mean_x=st.mean(X)
mean_y=st.mean(Y)

xy=sum( [X[i]*Y[i] for i in range(n)] )

sum_of_x=sum(X)
sum_of_y=sum(Y)

x_square=sum( [X[i]**2 for i in range(n)] )

slope=((n*xy)-sum_of_x*sum_of_y)/((n*x_square)-(sum_of_x**2))
intercept=mean_y-slope*mean_x

print(round(80*slope+intercept,3))