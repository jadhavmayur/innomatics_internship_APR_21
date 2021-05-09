# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern=r"(?<= )(&&|\|\|)(?= )"
replacement=lambda x:"and" if x.group()=="&&" else "or"

for i in range(int(input())):
    a=input()
    print(re.sub(pattern,replacement,a))