def isPrime(n):
    if n == 1 or n == 0  :
        return False
    if n == 2 :
        return True
    for i in range(2, int(n**0.5) + 1) :
        if n % i == 0 :
            return False
    else :
        return True

arr = [0 for i in range(123456*2+1)]

for i in range(len(arr)):
    if isPrime(i) == True :
        arr[i] += 1
        

while True :
    n = int(input())
    if n == 0 :
        break
    else :
        cnt = 0
        for i in range(n+1, 2*n+1):
            if arr[i] == 1:
                cnt += 1
        print(cnt)