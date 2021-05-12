import numpy as np



m=int(input())

a=np.array([input().split() for _ in range(m)],int)
b=np.array([input().split() for _ in range(m)],int)

print(np.dot(a,b))
 
