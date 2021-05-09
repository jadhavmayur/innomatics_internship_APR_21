# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pat1=r'(.*[A-Z]){2,}'
pat2=r'(.*[0-9]){3,}'
pat3=r'.*(.).*\1+.*'

for i in range(int(input())):
    N = input().strip()
    if N.isalnum() and len(N) == 10:
        if bool(re.search(pat1,N)) and bool(re.search(pat2,N)):
            if re.search(pat3,N):
                print('Invalid')
            else:
                print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')
                
    