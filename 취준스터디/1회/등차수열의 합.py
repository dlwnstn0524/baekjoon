n = int(input())
arr = list(map(int, input().split()))
arr1 = []
arr2 = []


if n == 1:
    print("YES")
    print(arr[0]+2)
    print(arr[0]-2)
else:   
    r = arr[1] - arr[0]
    flag = True
    for i in range(len(arr)-1):
        if arr[i] + r != arr[i+1]:
            print("NO")
            flag = False
            break
    if flag:
        print("YES")
        r1, r2 = r + 1, r
        f1, f2 = arr[0] + 1, -1
        for i in range(n):
            arr1.append(f1 + i*r1)
            arr2.append(f2 + i*r2)
        for i in range(n):
            print(arr1[i], end= " ")
        print()
        for i in range(n):
            print(arr2[i], end= " ")