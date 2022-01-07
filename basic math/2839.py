n = int(input())
num1 = int(n/5)
num2 = int(n/3)
arr = []
min = 10000

for i in range(num1+1):
    for j in range(num2 +1):
        if i*5 + j*3 == n:
            arr.append(i+j)
            break

for i in arr :
    if min > i:
        min =i

if min == 10000 :
    print(-1)
else :
    print(min)