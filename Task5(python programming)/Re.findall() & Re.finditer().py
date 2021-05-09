# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
a=input()
b=input()

comp=re.compile(b)
m=comp.search(a)

if not m:
    print("(-1, -1)")
while m:
    print("({0}, {1})".format(m.start(),m.end()-1))
    m= comp.search(a,m.start()+1)
