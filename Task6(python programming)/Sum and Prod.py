import numpy as np

m,n=map(int,input().split())

a=np.array([input().split() for _ in range(m)],int)


sum_arr=np.sum(a,axis=0)
prod_arr=np.prod(sum_arr,axis=0)
print(prod_arr)
