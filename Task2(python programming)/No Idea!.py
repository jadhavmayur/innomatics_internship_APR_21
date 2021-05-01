from six.moves import input as raw_input
n = raw_input().split()
n = map(int, n)
num= map(int, raw_input().split())
A = set(map(int, raw_input().split()))
B = set(map(int, raw_input().split()))

happiness = 0
for i in num:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1

print(happiness)