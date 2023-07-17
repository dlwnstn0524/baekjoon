n = int(input())
arr = list(map(int, input().split()))
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
        for i in range(n):
            print(arr[i] + (r-1)*i + 1, end = " ")
            arr2.append(arr[i] + (r-1)*i + 1)
        print()

        for j in range(n):
            print(arr[j] - arr2[j], end= " ")