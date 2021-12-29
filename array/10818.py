n = int(input())
arr = list(map(int, input().split()))
max = -1000000
min = 1000000

for i in arr :
    if max < i :
        max = i
    if min > i :
        min = i

print(min,max)
