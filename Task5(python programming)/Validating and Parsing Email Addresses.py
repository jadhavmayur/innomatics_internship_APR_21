# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re
a=int(input())

for i in range(a):
    name, email = input().split()
    s="<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
    if bool(re.match(s, email)):
        print(name,email)
    
    