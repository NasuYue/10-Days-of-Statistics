# Task
# The number of tickets purchased by each student for the University X vs. University Y football game follows a distribution that has a mean of mu=2.4 and a standard deviation of sigma=2.0. 
# A few hours before the game starts, 100 eager students line up to purchase last-minute tickets. If there are only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?

# >> Estimate sum of sample means

import statistics as st

mu=100*2.4
sigma=(100**0.5)*2.0

p=st.NormalDist(mu,sigma).cdf(250)

print(round(p,4))