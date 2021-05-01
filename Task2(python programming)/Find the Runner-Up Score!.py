if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list_arr=list(set(arr))
    sort_arr=sorted(list_arr)
    print(sort_arr[-2])