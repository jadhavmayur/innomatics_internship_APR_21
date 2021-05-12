import numpy as np
np.set_printoptions(legacy='1.13')


a=int(input())

b=np.array([input().split() for _ in range(a)], float)


    
print(round(np.linalg.det(b),2))


