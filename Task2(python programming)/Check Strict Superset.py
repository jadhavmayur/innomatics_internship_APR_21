from six.moves import input as raw_input
A=set(input().split())
n=int(input())
is_superset=True

for i in range(n):
    B=set(input().split())
    if not B.issubset(A):
        is_superset=False
    elif len(B)>=len(A):
        is_superset=False
    
   
        
print(is_superset)