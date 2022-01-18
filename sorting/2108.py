n = int(input())
arr = []
sum = 0
max = 0
result = []

for i in range(n):
    arr.append(int(input()))

arr.sort()

for i in arr :
    sum += i

print(sum/n)
print(arr[n//2])
if len(result) == 1 :
    print(result[0])
else :
    print(result[1])
print(max(arr)-min(arr))
