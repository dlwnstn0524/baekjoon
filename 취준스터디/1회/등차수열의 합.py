n = int(input())
arr = list(map(int, input().split()))
arr2 = []

r = arr[1] - arr[0]
flag = True
for i in range(len(arr)-1):
    if arr[i] + r != arr[i+1]:
        print("NO")
        flag = False
        break
if flag:
    print("YES")
    for i in arr:
        print(i+1, end = " ")
        arr2.append(i+1)
    print()
    print(arr2)
    for j in range(len(arr)):
        print(arr[j] - arr2[j], end=" ")