# Enter your code here. Read input from STDIN. Print output to STDOUT
from six.moves import input as raw_input
import sys
n=int(input())
e = list((map(int,raw_input().split())))

l=[]


for i in range(len(e)):
    for j in range(i+1,len(e)):
        if e[i]==e[j]:
            temp=e[i]
            e[j]=e[i]
            l.append(e[i])
        

        
        
set1=set(l)
set2=set(e)

captain_room=(set2)-(set1)
print(captain_room)