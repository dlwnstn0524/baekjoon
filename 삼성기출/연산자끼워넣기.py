import sys
input = sys.stdin.readline

def recur(depth, value):
    global arr, cals, M, m
    if depth == len(arr)-1:
        if value > M:
            M = value
        if value < m:
            m = value
        return
    else:
        for i in range(4):
            if cals[i] != 0:
                cals[i] -= 1
                if i == 0:
                    recur(depth + 1, value+arr[depth+1])
                elif i == 1:
                    recur(depth + 1, value - arr[depth + 1])
                elif i == 2:
                    recur(depth + 1, value * arr[depth + 1])
                elif i == 3:
                    recur(depth + 1, value // arr[depth + 1])
                cals[i] += 1

N = int(input())
arr = list(map(int, input().split()))
cals = list(map(int, input().split()))
m, M = 1000000000, -1000000000
recur(0, arr[0])
print(M)
print(m)