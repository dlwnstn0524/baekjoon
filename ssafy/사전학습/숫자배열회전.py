T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    
    arr_90 = []
    for i in zip(*arr):
        i = list(i)
        i.reverse()
        arr_90.append(''.join(list(map(str, i))))
    
    arr_180 = []
    for i in range(n):
        temp = arr[n-i-1]
        temp.reverse()
        arr_180.append(''.join(list(map(str, temp))))

    arr_270 = []
    for i in zip(*arr):
        i = list(i)
        arr_270.append(''.join(list(map(str, i))))
    
    print("#{}".format(test_case))
    for i in range(n):
        print(arr_90[i], arr_180[i], arr_270[i])