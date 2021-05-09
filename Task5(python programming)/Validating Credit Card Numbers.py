# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pat=r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$'
for i in range(int(input())):
    m= input().strip()
    find = re.search(pat,m)
    if find:
        d = "".join(find.group(0).split('-'))
        match = re.search(r'(\d)\1{3,}',d)
        if match:
            print('Invalid')
        else :
            print('Valid')
    else:
        print('Invalid')
                
    