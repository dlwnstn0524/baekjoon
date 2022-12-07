import math

n = int(input())

arr = [0 for i in range(15)]
cnt = 0

def dfs(idx):
    if idx == n :
        global cnt
        cnt += 1
        return

    for i in range(n):
        arr[idx] = i
        if isOk(idx):
            dfs(idx+1)

def isOk(idx) :
    for i in range(idx):
        if abs(arr[idx]-arr[i]) == abs(idx-i) or arr[idx] == arr[i] :
            return False
    return True

dfs(0)
print(cnt)