x, y, w, h = map(int, input().split())
arr = []
min = 1000
arr.append(x)
arr.append(y)
arr.append(w-x)
arr.append(h-y)

for i in arr :
    if min > i :
        min = i
print(min)