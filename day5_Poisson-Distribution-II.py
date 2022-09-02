# Task: The manager of a industrial plant is planning to buy a machine of either type A or type B. For each day’s operation:

# The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88. The daily cost of operating A is Ca=160+40*X^2 .
# - The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55. The daily cost of operating B is Cb=128+40*X^2 .
# Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure that they operate like new at the start of each day. Find and print the expected daily cost for each machine.

from math import factorial
from math import exp

k1=0.88
k2=1.55

p1_possion=(round(160+40*(k1+k1**2),3))
p2_possion=(round(128+40*(k2+k2**2),3))

print(p1_possion)
print(p2_possion)