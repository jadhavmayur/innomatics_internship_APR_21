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

f,g=map(int,input().split())

g=g
d=2
p_s=f/100
p_g=1-(f/100)

fact_ans=0
fact_ans2=0
for i in range(d,g+1):
  fact_ans+=comb(g,i)*pow(p_s,i)*pow(p_g,(g-i))
  

for i in range(0,d+1):
    fact_ans2+=comb(g,i)*pow(p_s,i)*pow(p_g,(g-i))
    

print("%.3f" % fact_ans2)
print("%.3f" % fact_ans)

