from six.moves import input as raw_input
n=int(input())
con=set()


for i in range(n):
    con.add(input())
    
distinct_stamp=len(con)    
print(distinct_stamp)