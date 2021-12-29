arr = []
cnt = 0
remainder = [0 for i in range(42)]

for i in range(10):
    arr.append(int(input()))

for i in range(10) :
    arr[i] = arr[i] % 42
    remainder[arr[i]] += 1

for i in remainder :
    if i !=0 :
        cnt += 1

print(cnt)