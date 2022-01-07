def is_prime_num(n):
    if n == 1 :
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0 :
            return False
    return True

m = int(input())
n = int(input())
arr = []
min = 100000
sum = 0

for i in range(m, n + 1):
    if is_prime_num(i) == True :
        arr.append(i)

for i in arr :
    if min > i :
        min = i
    sum += i

if sum == 0 :
    print("-1")
else :
    print(sum)
    print(min)