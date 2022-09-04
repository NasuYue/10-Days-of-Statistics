# Spearman's Rank Correlation Coefficient
# Reference: https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient
# Task: Given two n-element data sets, X and Y, calculate Spearman's rank correlation coefficient.

# Test sample
# n=10
# X=[10, 9.8, 8, 7.8, 7.7, 1.7, 6, 5, 1.4, 2]
# Y=[200, 44, 32, 24, 22, 17, 15, 12, 8, 4]

n=int(input())
X=list(map(float,input().split()))
Y=list(map(float,input().split()))

def genRank(data):
    # sort and unify data in order
    tmp=sorted(set(data))

    # Create dict {element:rank}
    rank_dict={}
    for rank_num,item in zip(range(1,n+1),tmp):
        rank_dict[item]=rank_num

    # Return rank to element list
    return [ rank_dict[x] for x in data ]

rank_x=genRank(X)
rank_y=genRank(Y)

# Caculate sum of covariance 
sum_of_d2=0
for rx,ry in zip(rank_x,rank_y):
    sum_of_d2+=(rx-ry)**2

# Spearman's Rank Correlation Coefficient Formula
corr_spearman=1-(6*sum_of_d2/(n*((n**2)-1)))

print(corr_spearman)