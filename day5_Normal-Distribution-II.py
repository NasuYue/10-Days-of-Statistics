# Task
# The final grades for a Physics exam taken by a large group of students have a mean of mu=70 and a standard deviation of sigma=10. If we can approximate the distribution of these grades by a normal distribution, what percentage of the students:
# 1. Scored higher than 80 (i.e., have a grade>80 )?
# 2. Passed the test (i.e., have a grade>=60)?
# 3. Failed the test (i.e., have a grade<60)?
# Find and print the answer to each question on a new line, rounded to a scale of 2 decimal places.

import statistics as st

mu=70
sigma=10

p1=1-st.NormalDist(mu,sigma).cdf(80)
p2=1-st.NormalDist(mu,sigma).cdf(60)
p3=st.NormalDist(mu,sigma).cdf(60)

print(round(p1*100,2)) #15.87
print(round(p2*100,2)) #84.13
print(round(p3*100,2)) #15.87