# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

m,s=map(int,input().split())

x=19.5
y1=20 
y2=22

less_than=0.5*(1+math.erf((x-m)/(s*math.sqrt(2))))

in_between=(0.5*(1+math.erf((y2-m)/(s*math.sqrt(2)))))-(0.5*(1+math.erf((y1-m)/(s*math.sqrt(2)))))

print("%.3f" % less_than)
print("%.3f" % in_between)