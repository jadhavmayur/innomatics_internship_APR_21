# Enter your code here. Read input from STDIN. Print output to STDOUT
from six.moves import input as raw_input
n=int(input())

for i in range(n):
    m=int(input())
    A=set(input().split())
    j=int(input())
    B=set(input().split())
    print(A.issubset(B))