# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s=r'([a-zA-Z0-9])\1'
m = re.search(s, input().strip())
print(m.group(1) if m else -1)