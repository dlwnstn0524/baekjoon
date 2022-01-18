n, m = map(int, input().split())
arr = list(map(int, input().split()))
var = []
near = 0

for i in range(len(arr)-2) :
    for j in range(i+1, len(arr)-1) :
        for k in range(j+1, len(arr)) :
            var.append(arr[i]+arr[j]+arr[k])

for i in var :
    if i <= m and m - near > m - i :
        near = i

print(near)