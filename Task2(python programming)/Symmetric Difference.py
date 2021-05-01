from six.moves import input as raw_input
num1 = int(raw_input())
set1 = set(map(int,raw_input().split()))
num2 = int(raw_input())
set2 = set(map(int,raw_input().split()))
set3 = (set1.difference(set2)).union(set2.difference(set1))

sort_list=list(sorted(set3))

for i in sort_list:
    print(i)