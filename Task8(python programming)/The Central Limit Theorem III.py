# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n=int(input())
mean=int(input())
sd=int(input())
dis=float(input())
z=float(input())

std=sd/pow(n,0.5)

print("%.2f"%(mean - std * z))
print("%.2f"%(mean + std * z))