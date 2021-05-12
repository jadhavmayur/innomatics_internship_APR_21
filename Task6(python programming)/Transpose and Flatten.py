import numpy as np



n,m=map(int,input().split())



a=np.array([input().split() for _ in range(n)],int)
    
print(np.transpose(a))
print(a.flatten())