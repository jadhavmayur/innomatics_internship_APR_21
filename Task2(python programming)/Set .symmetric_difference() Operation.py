# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
e = set(map(int, input().split()))
m =int(input())
f =set(map(int, input().split()))

sym_diff=len(e^f)
print(sym_diff)