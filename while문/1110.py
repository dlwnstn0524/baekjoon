n = int(input())
s = n / 10
i = n % 10
cnt = 0
while True :
    a = n / 10 + n % 10
    n = n % 10 * 10 + a % 10
    if n == a :
        break