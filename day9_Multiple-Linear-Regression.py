# Task: Find the value of Y for input sets.
# Regression line: Y=a+b1*x1+b2*x2

from sklearn import linear_model
import pandas as pd

# 1. Recevie dataset
# m = the number of observed features, e.q. [b1, b2, b3 ....]
# n = the number of feature sets 
m,n=map(int,input().split())

# df_train=[b1 , b2, Y]
train=[ list(map(float,input().split())) for i in range(n) ]
df_train=pd.DataFrame(train)

# q = the number of feature sets wants to query for
q=int(input())

# df_pred=[x1,x2]
pred=[list(map(float,input().split())) for i in range(q) ]
df_pred=pd.DataFrame(pred)

# 2. Split into x_train=[b1,b2], y_train=[Y]
x_train, y_train = df_train.iloc[:, :m], df_train.iloc[:, m]

# 3. Run linear regression model ~ [train,predict]
lm = linear_model.LinearRegression()
lm.fit(x_train,y_train)

# 4. Get parameters, y=a+b1*x1+b2*x2
# a = lm.intercept_
# b = lm.coef_
# print(a, b[0], b[1])

# 5. Predict Y with designed input df_pred=[x1,x2]
y_pred=lm.predict(df_pred)

for i in range(len(y_pred)):
    print(round(y_pred[i],2))