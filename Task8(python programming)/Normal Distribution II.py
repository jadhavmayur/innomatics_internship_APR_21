# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

m,s=map(int,input().split())

x=80
y1=60


greater_than_80=(0.5*(1-math.erf((x-m)/(s*math.sqrt(2)))))*100

greater_than_60=(0.5*(1-math.erf((y1-m)/(s*math.sqrt(2)))))*100

less_than_60=(0.5*(1+math.erf((y1-m)/(s*math.sqrt(2)))))*100

print("%.2f" % greater_than_80)
print("%.2f" % greater_than_60)
print("%.2f" % less_than_60)