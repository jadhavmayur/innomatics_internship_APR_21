# Enter your code here. Read input from STDIN. Print output to STDOUT
from six.moves import input as raw_input
import numpy as np
m,n = map(int,raw_input().split())
x = []
y =[]
for i in range(n):
    vals=list(map(float,raw_input().split()))
    x.append(vals[:-1])
    y.append(vals[-1])

q = int(raw_input())
test = []
for i in range(q):
    vals=list(map(float,raw_input().split()))
    test.append(vals)

x=np.insert(x,0,1,axis=1)
test=np.insert(test,0,1,axis=1)

tr=np.transpose(x)
e=np.dot(tr,x)
inv=np.linalg.inv(e)
f=np.dot(inv,tr)
b=np.dot(f,y)
final_ans=np.dot(test,b)
np.set_printoptions(precision=2)


for i in final_ans:
    print("%.2f"%i)