# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

a= int(input())
color_c = False
for _ in range(a):
    b= input()
    if '{' in b:
        color_c = True
    elif '}' in b:
        color_c = False
    elif color_c:
        for color in re.findall('#[0-9a-fA-F]{3,6}', b):
            print(color)
    