if __name__ == '__main__':
    N = int(input())
    arr=[]
    
    for i in range(N):
        method,*l=input().split()
        k=list(map(int,l))
        if len(k)==2:
            p=[k[0]]
            q=[k[1]]
        elif len(k)==1:
            p=[k[0]]
        if method=='insert':
            arr.insert(p[0],q[0])
        elif method=='append':
            arr.append(p[0])
        elif method=='remove':
            arr.remove(p[0])
        elif method=='sort':
            arr.sort()
        elif method=='pop':
            arr.pop()
        elif method=='reverse':
            arr.reverse()
        elif method=='print':
            print(arr)
        