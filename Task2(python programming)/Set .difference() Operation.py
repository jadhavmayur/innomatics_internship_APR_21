# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
e = set(map(int, input().split()))
m =int(input())
f =set(map(int, input().split()))

differ=len(e-f)
print(differ)