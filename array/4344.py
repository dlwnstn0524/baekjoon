n = int(input())

for i in range(n) :
    arr = list(map(int, input().split()))
    sum = 0
    cnt = 0
    avg = 0
    rate = 0
    for j in range(1, arr[0]+1):
        sum += arr[j]

    avg = sum / arr[0]

    for j in range(1, arr[0]+1):
        if arr[j] > avg :
            cnt += 1
    rate = cnt * 100 / arr[0]
    print("%0.3f%%" % rate)