import numpy as np

m,n=list(map(int, input().split()))
b = np.array([input().split() for _ in range(m)], int)
c = np.array([input().split() for _ in range(m)], int)

print(np.add(b,c))
print(np.subtract(b,c))
print(np.multiply(b,c))
print(np.floor_divide(b,c))
print(np.mod(b,c))
print(np.power(b,c))
