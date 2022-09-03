# Task
# A large elevator can transport a maximum of 9800 pounds. Suppose a load of cargo containing 49 boxes must be transported via the elevator. The box weight of this type of cargo follows a distribution with a mean of mu=205  pounds and a standard deviation of sigma=15 pounds. Based on this information, what is the probability that all 49 boxes can be safely loaded into the freight elevator and transported?

# Central limit theorem(CLT) refer to sample mean follows normal distribution as long as n is large enough.
# sample sum follows Norm(mu',std') 
# Sample mean mu' = n*mu; 
# sample std std' = sqrt(n)*sigma


import statistics as st

n=49
mu=205
sigma=15
max_weight=9800

mu_new=n*mu
sigma_new=(n**0.5)*sigma

print(mu_new)
print(sigma_new)
prob=st.NormalDist(mu_new,sigma_new).cdf(max_weight)

print(round(prob,4))
