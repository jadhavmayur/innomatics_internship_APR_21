# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
a=int(input())
start=r'((?=)^[789]\d{9})'
al=r"/^[A-Za-z]+$/"

for i in range(a):
    b=input()
    if bool(re.findall(start,b))==True and len(b)==10 and bool(re.findall(al,b))==False:
        print("YES")
    elif bool(re.findall(start,b))==True and len(b)==10 and bool(re.findall(al,b))==True:
        print("NO")
    else:
        print("NO")
    