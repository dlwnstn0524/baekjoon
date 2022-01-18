arr = [0 for i in range(1000001)]
temp = 0
result = []
min = 1000000

for i in range(1000001) :
    sum = 0
    sum += i
    i = str(i)
    for j in i:
        sum += ord(j) - ord("0")
    arr[int(i)] = sum

n = int(input())
for i in range(n):
    if arr[i] == n :
        result.append(i)

for i in result :
    if min > i :
        min = i

if min == 1000000 :
    print(0)
else :
    print(min)
