import sys
input = sys.stdin.readline
stairs = []
N = int(input())
for i in range(N):
    stairs.append(list(map(int, input().split())))

dp = [[1000000000] * 3 for _ in range(N)]
for i in range(3):
    if stairs[0][i] == 0:
        dp[0][i] = abs(1-i)
    else:
        continue

# 이중 포문이긴 하지만 두번째 포문의 반복 횟수가 3이라 크게 의미 없음 O(N*3)
for i in range(N):
    for j in range(3):
        if stairs[i][j] == 0:
            dp[i][j] = min(dp[i-1][0] + abs(j-0),
                           dp[i-1][1] + abs(j-1),
                           dp[i-1][2] + abs(j-2))

print(min(dp[-1]))