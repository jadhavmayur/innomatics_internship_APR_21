def swap_case(s):
    temp=''
    
    for i in s:
        if (i.isupper()==True):
            i.lower()
            temp+=i.lower()
        elif (i.islower()==True):
            i.upper()
            temp+=i.upper()
        else:
            temp+=i
            
    return temp

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result