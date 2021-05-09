# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
a=input()
pattern="[AEIOUaeiou]{2,}(?=[^aiueo])"
con="qwrtypsdfghjklzxcvbnm"
f=re.findall(pattern,a)

if f:
    for i in f:
        print(i)
else:
    print(-1)