if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    a = -101
    b = max(arr)
    
    for i in arr:
        if i>a and i<b:
            a=i
    print(a)
