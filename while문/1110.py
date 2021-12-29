n = int(input())
first = n
cnt = 0

while True :
    cnt += 1
    temp = n % 10 + int(n /10)
    n = n % 10 * 10 + temp % 10
    if n == first :
        print(cnt)
        break