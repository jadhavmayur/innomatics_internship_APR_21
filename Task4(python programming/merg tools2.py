def merge_the_tools(string, k):
    # your code goes here
    chunk,chunk_size=len(string),len(string)//k
    sp=[string[i:i+chunk_size] for i in range(0,chunk,chunk_size)]
    set1=set()
    for i in sp:
        print(''.join(sorted(set(i), key=i.index)))
          

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)