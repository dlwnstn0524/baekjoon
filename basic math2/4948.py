def isPrime(num) :
    if num == 1 :
        return False
    else :
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0 :
                return False
        return True

def countPrime(n) :
    cnt = 0
    for i in range(n+1, 2*n+1):
        if isPrime(i) == True :
            cnt += 1
    print(cnt)

while True :
    n = int(input())
    if n == 0 :
        break
    else :
        countPrime(n)
