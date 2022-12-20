import sys

def fib(n):
    global cnt_recursive
    if n == 1 or n ==2 :
        cnt_recursive += 1
        return 1
    else :
        return fib(n-1) + fib(n-2)
def fibo(n):
    global cnt_dp
    f = [0 for _ in range(41)]
    f[0] = 0
    f[1] = 1
    f[2] = 1
    for i in range(3,n+1):
        cnt_dp += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

cnt_recursive = 0
cnt_dp = 0

n = int(sys.stdin.readline())
fib(n)
fibo(n)
print(cnt_recursive, cnt_dp)