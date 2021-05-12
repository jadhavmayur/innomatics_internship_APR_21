import numpy as np




m,n=map(int,input().split())

a=np.array([input().split() for _ in range(m)],int)

mean_a=np.mean(a,axis=1)
print(mean_a)

var_a=np.var(a,axis=0)
print(var_a)

np.set_printoptions(legacy='1.13')
print(np.std(a,axis = None))
 
