n = int(input())
s = set(map(int, input().split()))
m=int(input())


for i in range(m):
    method,*l=input().split()
    k=list(map(int,l))
    if len(k)==2:
        p=[k[0]]
        q=[k[1]]
    elif len(k)==1:
        p=[k[0]]
    if method=='remove':
        s.remove(p[0])
    elif method=='discard':
        s.discard(p[0])
    elif method=='pop':
        s.pop()
    
        
        



print(sum(list(s)))