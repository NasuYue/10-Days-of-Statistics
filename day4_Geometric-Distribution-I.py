# Negative Binomial Distribution:
# pmf = b*(x,n,p) = (n-1 x-1)!*(p**x)*(q**(n-x)), where p=hits; q=1-p; n=trials; x=number of success;
# Geometric Distribution: 
# g(n,p)=q**(n-1)*p, where p=hits; q=1-p; n=trials;
# The geometric distribution is a negative binomial distribution where the number of successes is 1 

# Task:
# The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect occurs the 5th item produced?

import sys
from math import factorial

line1=list(map(int, input().split()))
line2=list(map(int, input().split()))

p=line1[0]/line1[1]
x=1
n=line2[0]

# Negative Binomial Distribution pmf
p_negative_binomial=(
            factorial(n-1) / (factorial(x-1) * factorial(n-x))
            *(p**x)
            *((1-p)**(n-x))
)

# The geometric distribution is a negative binomial distribution where the number of successes is 1 
p_geometric=(1-p)**(n-1)*p

print(round(p_negative_binomial,3))
print(round(p_geometric,3))