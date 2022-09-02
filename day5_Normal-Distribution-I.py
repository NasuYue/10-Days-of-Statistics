# In a certain plant, the time taken to assemble a car is a random variable, X, having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours. What is the probability that a car can be assembled at this plant in:
# 1. Less than 19.5 hours?
# 2. Between 20 and 22 hours?

from statistics import NormalDist

mu=20
sigma=2

p1=NormalDist(mu,sigma).cdf(19.5)
p2=NormalDist(mu,sigma).cdf(22)-NormalDist(mu,sigma).cdf(20)

print(round(p1,3))
print(round(p2,3))