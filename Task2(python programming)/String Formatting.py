# Enter your code here. Read input from STDIN. Print output to STDOUT
from six.moves import input as raw_input
n=int(input())

m=set(map(int,input().split()))
p=int(input())
      


      
for i in range(p):
    method=input().split()[0]
    temp = set(map(int,raw_input().split()))
    if method=='intersection_update':
        m.intersection_update(temp)
    elif method=='update':
        m.update(temp)
    elif method=='symmetric_difference_update':
        m.symmetric_difference_update(temp)
    elif method=='difference_update':
        m.difference_update(temp)


print(sum(m))  