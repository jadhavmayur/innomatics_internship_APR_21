# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import sqrt,phase
a=complex(input())

r=sqrt((a.real**2)+(a.imag**2)).real
phase=phase(complex(a.real,a.imag))

print(r)
print(phase)