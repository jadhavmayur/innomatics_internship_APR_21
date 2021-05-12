import numpy as np

m,n=map(int,input().split())

a=np.array([input().split() for _ in range(m)],int)

min_a=np.min(a,axis=1)

print(np.max(min_a))
 
