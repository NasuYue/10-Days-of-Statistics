# Task
# The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect is found during the first 5 inspections?

from math import factorial

# input: 1 3 5
line1=list(map(int, input().split()))
line2=list(map(int, input().split()))

p=line1[0]/line1[1]
x=1
n=[i for i in range(1,line2[0]+1) ] # 12345

# Negative Binomial Distribution pmf for n=1~5
p_negative_binomial=0
for i in n:
    p_negative_binomial+=(
                factorial(i-1) / (factorial(x-1) * factorial(i-x))
                *(p**x)
                *((1-p)**(i-x))
    )

print(round(p_negative_binomial,3))