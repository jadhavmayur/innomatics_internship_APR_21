if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    m=[]
    for i in integer_list:
        m.append(i)
    
    T=tuple(m)
    print(hash(T))
        