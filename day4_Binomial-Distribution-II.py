#Task
#A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:
# 1. No more than 2 rejects?
# 2. At least 2 rejects?

# b(x,n,p)=(n!/(n-x)!x!)*(p**x)*(q**(n-x))
# p=hit rate; q=1-p; n=trials; x=designed outcome

from math import factorial

args = list(map(int, input().split()))

n=args[1]
p=float(args[0]/100)

x1=[0,1,2]
x2=[i for i in range(2,11)] #2~10

prob1, prob2 = 0,0

for i in x1:
    prob1+=(factorial(n)/(factorial(n-i)*factorial(i)))*(p**i)*((1-p)**(n-i))
    
for i in x2:
    prob2+=(factorial(n)/(factorial(n-i)*factorial(i)))*(p**i)*((1-p)**(n-i))
    
print(round(prob1,3))
print(round(prob2,3))