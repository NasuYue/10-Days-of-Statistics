# Pearson correlation coefficient
# Wiki: https://en.wikipedia.org/wiki/Pearson_correlation_coefficient
# Given two n-element data sets, X and Y, calculate Pearson correlation coefficient.
import statistics as stats

# Test sampe
# n=10
# X=[10, 9.8, 8, 7.8, 7.7, 7, 6, 5, 4, 2]
# Y=[200, 44, 32, 24, 22, 17, 15, 12, 8, 4]

n=int(input())
X=list(map(float,input().split()))
Y=list(map(float,input().split()))

mean_x=round(sum(X)/len(X),3)
mean_y=round(sum(Y)/len(Y),3)

# Be aware: use population stdev pstdev()
std_x=round(stats.pstdev(X),3)
std_y=round(stats.pstdev(Y),3)

sum_of_covar=0
for i in range(n):
    sum_of_covar+=(X[i]-mean_x)*(Y[i]-mean_y)

corr=round(sum_of_covar/(std_x*std_y*n),3)

print(corr)