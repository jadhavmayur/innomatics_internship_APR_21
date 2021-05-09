def solve(s):
    first,last=s.split()
    c_name=''
    c_last=''
    for i in range(len(s)):
        if first[0].islower()==True:
            c_name=first[0].upper()+first[1:]
        if last[0].islower()==True:
            c_last=last[0].upper()+last[1:]
    return print(c_name+' '+c_last)          
            

n='mayur jadhav'
solve(n)
    