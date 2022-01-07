def isPrime(n): #소수 구하는 함수 구현
    if n == 0 or n == 1 :
        return False
    elif n == 2 :
        return True
    for i in range(2, n):
        if n % i == 0 :
            return False
    return True
    
arr = [0 for i in range(10001)] #해당 숫자가 소수인지 아닌지 담겨있는 배열 생성
for i in range(len(arr)):
    if isPrime(i) == True :
        arr[i] = 1

t = int(input()) # 테스트 케이스 입력 받기

for i in range(t) :
    n = int(input()) # 짝수 n 입력
    result = []
    max = 0
    for j in range(2, int(n/2) + 1) :
        for k in range(int(n/2), n) :
            if arr[j] == 1 and arr[k] == 1 and j + k == n :
                result.append(j)
                break
    for j in result :
        if max < j :
            max = j
    print(max, n - max)
