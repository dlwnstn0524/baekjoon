import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    if N > 5 :
        for i in range(6, N+1):
            dp[i] = dp[i-1] + dp[i-5]
        print(dp[N])
    else :
        print(dp[N])