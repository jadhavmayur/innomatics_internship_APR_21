def average(array):
    # your code goes here
    set_array=list(set(array))
    n=len(set_array)
    sum_=sum(set_array)
    avg=(sum_/n)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
        