# Enter your code here. Read input from STDIN. Print output to STDOUT
from six.moves import input as raw_input
X=[]
Y=[]
N=5

for i in range(N):
    x,y=map(int,raw_input().split())    #strip().
    X.append(x)
    Y.append(y)
    
import math

def pear_corr_coef(X,Y):
  data_size=N
  mu_X=sum(X)/data_size
  mu_Y=sum(Y)/data_size
  sigma_X=(sum([(i - mu_X)**2 for i in X]) /data_size)**0.5
  sigma_Y=(sum([(i - mu_Y)**2 for i in Y]) /data_size)**0.5
  cov=sum([(X[i]-mu_X)*(Y[i]-mu_Y) for i in range(data_size)])
  pearson_corr=cov/(data_size*sigma_X*sigma_Y)
  return round(pearson_corr,3)



mu_X=sum(X)/N
mu_Y=sum(Y)/N
sigma_X=(sum([(i - mu_X)**2 for i in X]) /N)**0.5
sigma_Y=(sum([(i - mu_Y)**2 for i in Y]) /N)**0.5

p=pear_corr_coef(X,Y)
b=p*(sigma_Y/sigma_X)
a=((mu_Y)-b*(mu_X))

print("%.3f"%(a + b*80))