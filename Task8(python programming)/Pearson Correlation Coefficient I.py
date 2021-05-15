# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

data_size=int(input())
X=list(map(float,input().split()))
Y=list(map(float,input().split()))
mu_X=sum(X)/data_size

mu_Y=sum(Y)/data_size



sigma_X=(sum([(i - mu_X)**2 for i in X]) /data_size)**0.5
sigma_Y=(sum([(i - mu_Y)**2 for i in Y]) /data_size)**0.5


 
cov=sum([(X[i]-mu_X)*(Y[i]-mu_Y) for i in range(data_size)])

pearson_corr=cov/(data_size*sigma_X*sigma_Y)

print("%.3f" % pearson_corr)
