arr = []

for i in range(9) :
    arr.append(int(input()))

max = 0
max_i = 1

for i in range(9) :
    if max < arr[i] :
        max = arr[i]
        max_i = i+1

print(max)
print(max_i)
