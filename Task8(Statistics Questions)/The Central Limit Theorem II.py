# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

pd=int(input())
sample=int(input())
m=int(input())
sd=int(input())
samle_sd=math.sqrt(sample)*sd
mean_sample = m * sample



def clf(pd, mean, sd):
  return 0.5 * (1 + math.erf((pd - mean) / (sd * (2 ** 0.5))))



print(round(clf(pd, mean_sample, samle_sd), 4))