n = int(input())
arr = []

for i in range(666, 1000000000):
    if '666' in str(i) :
        arr.append(i)
    if len(arr) == n :
        print(arr[n-1])
        break