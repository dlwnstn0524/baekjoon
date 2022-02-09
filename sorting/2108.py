import math

n = int(input())
arr = []
sum = 0
MAX = 0
cnt = []
cnt2 = []

for i in range(n):
    arr.append(int(input()))

arr.sort()
temp = set(arr)
temp = list(temp)

for i in temp:
    cnt.append([i])
cnt.sort()
for i in cnt:
    i.append(arr.count(i[0]))

    
for i in arr:
    sum += i

for i in cnt :
    if MAX < i[1] :
        MAX = i[1]

for i in cnt :
    if MAX == i[1]:
        cnt2.append(i[0])

print(round(sum/n))
print(arr[n//2])
if len(cnt2) == 1 :
    print(cnt2[0])
else :
    print(cnt2[1])

print(max(arr)-min(arr))
