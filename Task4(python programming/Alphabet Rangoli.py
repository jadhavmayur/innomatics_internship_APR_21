def print_rangoli(size):
    # your code goes here
    n=size
    char=list(map(chr,range(97,123)))
    s=char[n-1::-1]+char[1:n]  #x=l[n-1::-1]+l[1:n]
    l1=len('-'.join((s)))
    
    for i in range(1,n):
        print('-'.join(char[n-1:n-i:-1]+char[n-i:n]).center(l1,'-'))
        
    for i in range(n,0,-1):
        print('-'.join(char[n-1:n-i:-1]+char[n-i:n]).center(l1,'-'))
    
    
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)