# A random variable, X, follows Poisson distribution with mean of 2.5. Find the probability with which the random variable X is equal to 5.
# Poisson random variable: p(k,l)=(l**k)*(exp(1)**(-l))/factorial(k)
from math import factorial
from math import exp

l=2.5
k=5

p_possion=(l**k)*(exp(1)**(-l))/factorial(k)

print(p_possion)