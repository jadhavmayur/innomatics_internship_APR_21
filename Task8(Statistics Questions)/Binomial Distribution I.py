# Enter your code here. Read input from STDIN. Print output to STDOUT
def fact(a):
  fact_a=1
  for i in range(1,a+1):
    fact_a=fact_a*i
  return fact_a

def comb(a,b):
  
  m=fact(a)
  
  n=fact(b)
  
  r=fact(a-b)
  
  comb=m/(n*r)
  return comb

b,g=map(float,input().split())
n=6
r=3
p_b=b/(b+g)
p_g=g/(b+g)

fact_ans=0
for i in range(r,n+1):
  fact_ans+=comb(n,i)*pow(p_b,i)*pow(p_g,(n-i))




print("%.3f" % fact_ans)

