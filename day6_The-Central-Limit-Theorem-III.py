# Task
# You have a sample of 100 values from a population with mean  mu=500 and with standard deviation sigma=80. Compute the interval that covers the middle 95% of the distribution of the sample mean; in other words, compute A and B such that P(A<X<B)=0.95. Use the value of . Note that z=1.96 is the z-score.

# From population to estimate smaple confidential interval
# CI=[mu-1.96*std,mu+1.96*std]

n=100
mu=500
sigma=80
z=1.96

mu_sample=mu
sigma_sample=sigma/(n**0.5)

lower_cutoff=mu_sample-z*sigma_sample
upper_cutoff=mu_sample+z*sigma_sample

print(round(lower_cutoff,2))
print(round(upper_cutoff,2))